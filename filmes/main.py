"""Ponto de entrada do projeto."""

from agent import executar_agente


def main() -> None:
    print("Agente de Filmes com loop ReAct manual")
    print("Digite 'sair' para encerrar.\n")

    while True:
        pergunta = input("Pergunta: ").strip()

        if pergunta.lower() in {"sair", "exit", "quit"}:
            print("Encerrando o agente.")
            break

        if not pergunta:
            print("Digite uma pergunta válida.\n")
            continue

        resposta = executar_agente(pergunta)
        print("\n" + resposta + "\n")


if __name__ == "__main__":
    main()
