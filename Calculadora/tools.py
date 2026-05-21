import math


def operacoes_basicas(a: float, b: float, operacao: str):
    """Realiza soma, subtração, multiplicação e divisão."""
    if operacao == "soma":
        return a + b
    if operacao == "subtracao":
        return a - b
    if operacao == "multiplicacao":
        return a * b
    if operacao == "divisao":
        return a / b if b != 0 else "Erro: divisão por zero"
    return "Erro: operação inválida"


def calcular_area_circulo(raio: float):
    """Calcula a área de um círculo."""
    return math.pi * (raio ** 2)


TOOLS = {
    "operacoes_basicas": operacoes_basicas,
    "calcular_area_circulo": calcular_area_circulo,
}