import csv
from filme import Filme

def carregar_filmes(caminho):
    filmes = []

    with open(caminho, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            filme = Filme(
                linha["titulo"],
                int(linha["ano"]),
                linha["genero"],
                linha["diretor"],
                float(linha["nota"])
            )
            filmes.append(filme)

    return filmes

def salvar_filmes(caminho, filmes):
    with open(caminho, mode="w", encoding="utf-8", newline="") as arquivo:
        campos = ["titulo", "ano", "genero", "diretor", "nota"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        escritor.writeheader()

        for filme in filmes:
            escritor.writerow({
                "titulo": filme.titulo,
                "ano": filme.ano,
                "genero": filme.genero,
                "diretor": filme.diretor,
                "nota": filme.nota
            })