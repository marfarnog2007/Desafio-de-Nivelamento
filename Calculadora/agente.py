import google.generativeai as genai
from tools import operacoes_basicas, calcular_area_circulo

# Configure sua API Key aqui
genai.configure(api_key='AIzaSyC2bJmQ1fQ9scYi3iFI-uC8txt9tF6q1EE')

model = genai.GenerativeModel(
    model_name='models/gemini-1.5-flash'
)

def executar_agente(pergunta):
    chat = model.start_chat(enable_automatic_function_calling=True)
    response = chat.send_message(pergunta)
    return response.text

# Exemplo de uso
if __name__ == "__main__":
    print(executar_agente("Quanto é 152 multiplicado por 4?"))
    print(executar_agente("Qual a área de um círculo com raio 5?"))
