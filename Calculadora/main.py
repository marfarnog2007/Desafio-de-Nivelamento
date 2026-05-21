from agent import executar_agente

if __name__ == "__main__":
    pergunta = input("Digite sua pergunta: ")
    resposta = executar_agente(pergunta)
    print("\nResposta final:")
    print(resposta)

    