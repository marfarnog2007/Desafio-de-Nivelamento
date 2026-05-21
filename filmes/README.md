# Agente de Filmes com ReAct Manual

Este projeto implementa um agente de IA sobre o tema **filmes**, usando o Gemini e ferramentas Python locais. O objetivo é mostrar, de forma explícita no código, como funciona o ciclo de raciocínio de um agente.

## O que o agente faz

O agente responde perguntas sobre filmes usando ferramentas próprias. Ele pode:

- Buscar informações de um filme pelo título;
- Listar filmes por gênero;
- Recomendar filmes por gênero e nota mínima;
- Comparar dois filmes por nota, duração, ano, gênero e diretor.

Exemplos de perguntas:

```text
Me recomende filmes de ficção científica com nota acima de 8.5
Compare Interestelar e A Origem
Qual é a sinopse de Cidade de Deus?
Liste filmes de drama
```

## Estrutura do projeto

```text
agente_filmes_corrigido/
├── agent.py          # Configuração do modelo, system prompt e loop ReAct manual
├── main.py           # Ponto de entrada e interação com o usuário
├── tools.py          # Funções de ferramenta usadas pelo agente
├── requirements.txt  # Dependências do projeto
├── .env              # Exemplo de variáveis de ambiente
├── .gitignore        # Arquivos que não devem ser versionados
└── README.md         # Documentação do projeto
```



## Como instalar

```bash
pip install -r requirements.txt
```

## Como executar

```bash
python main.py
```

Depois, digite uma pergunta sobre filmes. Para encerrar, digite:

```text
sair
```

## Como funciona o loop ReAct

O arquivo `agent.py` implementa o ciclo manualmente. O modelo recebe a pergunta e deve retornar um JSON com uma decisão.

Quando precisa usar uma ferramenta, ele retorna:

```json
{
  "thought": "Preciso buscar os dados do filme informado.",
  "action": "buscar_filme",
  "action_input": {"titulo": "Interestelar"}
}
```

O código executa a ferramenta e devolve o resultado como `Observation`. Depois disso, o modelo pode chamar outra ferramenta ou gerar a resposta final:

```json
{
  "thought": "Agora tenho os dados necessários para responder.",
  "answer": "Interestelar é um filme de ficção científica dirigido por Christopher Nolan..."
}
```

Papel dos agentes

- **Thought:** o modelo explica o próximo passo;
- **Action:** o modelo escolhe qual ferramenta usar;
- **Action Input:** o modelo informa os parâmetros da ferramenta;
- **Observation:** o código executa a ferramenta e retorna o resultado;
- **Answer:** o modelo responde ao usuário com base nas observações.

## Ferramentas disponíveis

As ferramentas estão em `tools.py`:

| Ferramenta | Função |
|---|---|
| `buscar_filme` | Busca um filme pelo título |
| `listar_filmes_por_genero` | Lista filmes por gênero |
| `recomendar_filmes` | Recomenda filmes por gênero e nota mínima |
| `comparar_filmes` | Compara dois filmes |

## Dificuldades e aprendizados

 Quando o SDK faz chamadas automáticas de função, o código fica menor, mas o funcionamento interno do agente fica escondido. Implementar o ReAct manualmente exigiu pensar em como o modelo deve responder, como interpretar essa resposta, como executar a ferramenta correta e como devolver a observação para o próximo passo.

Outro aprendizado importante foi separar responsabilidades. O arquivo `tools.py` deve conter apenas ferramentas, o `agent.py` deve conter a lógica do agente e o `main.py` deve cuidar apenas da interação com o usuário. Essa separação facilita a manutenção.



