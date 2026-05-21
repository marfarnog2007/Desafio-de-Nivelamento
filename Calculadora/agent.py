from google import genai
from google.genai import errors


API_KEY = "AIzaSyCs5rIu14dpfLoN_g5gafaQ4IQKX8kM6Vg"
client = genai.Client(api_key=API_KEY)


chat = client.chats.create(model="gemini-2.0-flash")

def executar_agente(pergunta):
    try:
        # Envia a mensagem usando a nova sintaxe da biblioteca google-genai
        response = chat.send_message(pergunta)
        return response.text
    
    except errors.APIError as e:
        # Captura especificamente o erro de limite estourado (429) e avisa o usuário
        if e.code == 429:
            return "Ops! O limite de requisições gratuitas foi atingido. Aguarde cerca de 15 segundos e tente novamente."
        return f"Erro na API do Gemini: {e.message}"
        
    except Exception as e:
        return f"Ocorreu um erro inesperado: {e}"