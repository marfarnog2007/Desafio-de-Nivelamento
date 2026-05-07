# Desafio-de-Nivelamento

## O que o agente faz:  
Uma calculadora inteligente para resolver cálculos matemáticos e geométricos.

## Ferramentas Escolhidas:   
1) operacoes_basicas: Escolhida para garantir que a LLM não erre cálculos aritméticos simples (alucinação).

2) calcular_area_circulo: Demonstra a capacidade do agente de aplicar fórmulas matemáticas específicas usando bibliotecas como math.

  ## Como rodar:
 1) É necessário que o link do repositório seja clonado, com isso , coloque git clone [link], e depois,cd [nome da pasta]
 2) instalar as dependencias: pip install -r requirements.txt
 3) No arquivo agente.py, onde configura sua API key, inserir a chave da API, podendo ser Gemini ou OpenAI
 4) Depois de colocar para rodar, no terminal coloque : python agente.py
## Dificuldades e Aprendizados:
sem o LangChain, foi mais difícil estruturar o dicionario de ferramentas, por exemplo.
