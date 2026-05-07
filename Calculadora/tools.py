def operacoes_basicas(a: float, b: float, operacao: str):
    """Realiza operações de soma, subtração, multiplicação e divisão."""
    if operacao == "soma": return a + b
    if operacao == "subtracao": return a - b
    if operacao == "multiplicacao": return a * b
    if operacao == "divisao": return a / b if b != 0 else "Erro: Divisão por zero"

def calcular_area_circulo(raio: float):
    """Calcula a área de um círculo dado o raio (A = π * r²)."""
    import math
    area = math.pi * (raio ** 2)
    return f"A área do círculo com raio {raio} é {area:.2f}"
