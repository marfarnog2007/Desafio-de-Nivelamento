"""Configuração do modelo e loop ReAct manual do agente."""

from __future__ import annotations

import json
import os
from typing import Any

from dotenv import load_dotenv
from google import genai
from google.genai import errors

from tools import TOOLS, TOOLS_DESCRICAO


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY não encontrada. Crie um arquivo .env local com GEMINI_API_KEY=sua_chave."
    )

client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = f"""

{{
  "thought": "raciocínio curto sobre o próximo passo",
  "action": "nome_da_ferramenta",
  "action_input": {{"parametro": "valor"}}
}}

Quando tiver a resposta final:
{{
  "thought": "raciocínio curto final",
  "answer": "resposta final para o usuário"
}}



{TOOLS_DESCRICAO}
"""


def _extrair_json(texto: str) -> dict[str, Any]:
    """Tenta converter a resposta do modelo em JSON válido."""
    texto = texto.strip()

    if texto.startswith("```"):
        texto = texto.replace("```json", "").replace("```", "").strip()

    return json.loads(texto)


def _executar_ferramenta(nome: str, argumentos: dict[str, Any]) -> Any:
    """Executa uma ferramenta cadastrada no dicionário TOOLS."""
    if nome not in TOOLS:
        return {"erro": f"Ferramenta inválida: {nome}"}

    try:
        return TOOLS[nome](**argumentos)
    except TypeError as erro:
        return {"erro": f"Argumentos inválidos para {nome}: {erro}"}
    except Exception as erro:
        return {"erro": f"Erro ao executar {nome}: {erro}"}


def executar_agente(pergunta: str, max_iteracoes: int = 5, mostrar_passos: bool = True) -> str:
    """Executa o loop ReAct manual: Thought -> Action -> Observation -> Answer."""
    historico = [
        {"role": "user", "parts": [{"text": SYSTEM_PROMPT}]},
        {"role": "model", "parts": [{"text": "Entendido. Vou responder usando o ciclo ReAct em JSON."}]},
        {"role": "user", "parts": [{"text": f"Pergunta: {pergunta}"}]},
    ]

    passos: list[str] = []

    try:
        for numero_iteracao in range(1, max_iteracoes + 1):
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=historico,
            )

            texto_modelo = response.text or "{}"
            historico.append({"role": "model", "parts": [{"text": texto_modelo}]})

            try:
                decisao = _extrair_json(texto_modelo)
            except json.JSONDecodeError:
                return "Erro: o modelo não retornou um JSON válido para o ciclo ReAct."

            thought = decisao.get("thought", "")

            if "answer" in decisao:
                if mostrar_passos and passos:
                    return "\n".join(passos) + f"\n\nResposta final:\n{decisao['answer']}"
                return decisao["answer"]

            action = decisao.get("action")
            action_input = decisao.get("action_input", {})

            if not action:
                return "Erro: o modelo não informou uma ação nem uma resposta final."

            observacao = _executar_ferramenta(action, action_input)

            if mostrar_passos:
                passos.append(
                    f"Iteração {numero_iteracao}\n"
                    f"Thought: {thought}\n"
                    f"Action: {action}\n"
                    f"Action Input: {action_input}\n"
                    f"Observation: {observacao}"
                )

            historico.append(
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": "Observation: "
                            + json.dumps(observacao, ensure_ascii=False)
                            + "\nContinue o ciclo ReAct. Use outra ação ou gere a resposta final."
                        }
                    ],
                }
            )

        return "Erro: número máximo de iterações atingido antes da resposta final."

    except errors.APIError as erro:
        if getattr(erro, "code", None) == 429:
            return "Limite de requisições atingido. Tente novamente em instantes."
        return f"Erro na API do Gemini: {getattr(erro, 'message', str(erro))}"
    except Exception as erro:
        return f"Erro inesperado: {erro}"
