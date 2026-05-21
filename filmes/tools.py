"""Ferramentas do agente de filmes.

Este arquivo concentra somente as funções que o agente pode executar.
Nenhuma regra de conversa, configuração de modelo ou entrada de usuário deve ficar aqui.
"""

from __future__ import annotations

from typing import Any


FILMES = [
    {
        "titulo": "Interestelar",
        "ano": 2014,
        "genero": "ficção científica",
        "diretor": "Christopher Nolan",
        "nota": 8.7,
        "duracao_min": 169,
        "sinopse": "Um grupo de astronautas viaja por um buraco de minhoca em busca de um novo lar para a humanidade.",
    },
    {
        "titulo": "A Origem",
        "ano": 2010,
        "genero": "ficção científica",
        "diretor": "Christopher Nolan",
        "nota": 8.8,
        "duracao_min": 148,
        "sinopse": "Um ladrão especializado em invadir sonhos recebe a missão de implantar uma ideia na mente de uma pessoa.",
    },
    {
        "titulo": "O Poderoso Chefão",
        "ano": 1972,
        "genero": "drama",
        "diretor": "Francis Ford Coppola",
        "nota": 9.2,
        "duracao_min": 175,
        "sinopse": "A história da família Corleone e sua influência no crime organizado nos Estados Unidos.",
    },
    {
        "titulo": "Parasita",
        "ano": 2019,
        "genero": "suspense",
        "diretor": "Bong Joon-ho",
        "nota": 8.5,
        "duracao_min": 132,
        "sinopse": "Uma família pobre se infiltra na vida de uma família rica, gerando consequências inesperadas.",
    },
    {
        "titulo": "Toy Story",
        "ano": 1995,
        "genero": "animação",
        "diretor": "John Lasseter",
        "nota": 8.3,
        "duracao_min": 81,
        "sinopse": "Brinquedos ganham vida quando os humanos não estão por perto.",
    },
    {
        "titulo": "Cidade de Deus",
        "ano": 2002,
        "genero": "drama",
        "diretor": "Fernando Meirelles e Kátia Lund",
        "nota": 8.6,
        "duracao_min": 130,
        "sinopse": "A ascensão do crime organizado em uma comunidade do Rio de Janeiro vista pelos olhos de Buscapé.",
    },
]


def _normalizar(texto: str) -> str:
    return texto.strip().lower()


def buscar_filme(titulo: str) -> dict[str, Any]:
    """Busca um filme pelo título ou por parte do título."""
    titulo_normalizado = _normalizar(titulo)

    for filme in FILMES:
        if titulo_normalizado in _normalizar(filme["titulo"]):
            return filme

    return {"erro": f"Filme não encontrado: {titulo}"}


def listar_filmes_por_genero(genero: str) -> list[dict[str, Any]]:
    """Lista filmes cadastrados de um determinado gênero."""
    genero_normalizado = _normalizar(genero)

    resultados = [
        filme for filme in FILMES
        if genero_normalizado in _normalizar(filme["genero"])
    ]

    return resultados or [{"erro": f"Nenhum filme encontrado para o gênero: {genero}"}]


def recomendar_filmes(genero: str | None = None, nota_minima: float = 0) -> list[dict[str, Any]]:
    """Recomenda filmes por gênero opcional e nota mínima."""
    resultados = FILMES

    if genero:
        genero_normalizado = _normalizar(genero)
        resultados = [
            filme for filme in resultados
            if genero_normalizado in _normalizar(filme["genero"])
        ]

    resultados = [filme for filme in resultados if filme["nota"] >= nota_minima]
    resultados = sorted(resultados, key=lambda filme: filme["nota"], reverse=True)

    return resultados[:3] or [{"erro": "Nenhuma recomendação encontrada com esses critérios."}]


def comparar_filmes(titulo_1: str, titulo_2: str) -> dict[str, Any]:
    """Compara dois filmes por nota, duração, ano, gênero e diretor."""
    filme_1 = buscar_filme(titulo_1)
    filme_2 = buscar_filme(titulo_2)

    if "erro" in filme_1:
        return filme_1
    if "erro" in filme_2:
        return filme_2

    return {
        "filme_1": filme_1,
        "filme_2": filme_2,
        "maior_nota": filme_1["titulo"] if filme_1["nota"] > filme_2["nota"] else filme_2["titulo"],
        "mais_curto": filme_1["titulo"] if filme_1["duracao_min"] < filme_2["duracao_min"] else filme_2["titulo"],
    }


TOOLS = {
    "buscar_filme": buscar_filme,
    "listar_filmes_por_genero": listar_filmes_por_genero,
    "recomendar_filmes": recomendar_filmes,
    "comparar_filmes": comparar_filmes,
}

TOOLS_DESCRICAO = """
Ferramentas disponíveis:
1. buscar_filme(titulo: str): busca detalhes de um filme pelo título.
2. listar_filmes_por_genero(genero: str): lista filmes cadastrados de um gênero.
3. recomendar_filmes(genero: str | None = None, nota_minima: float = 0): recomenda até 3 filmes por gênero e nota mínima.
4. comparar_filmes(titulo_1: str, titulo_2: str): compara dois filmes.
"""
