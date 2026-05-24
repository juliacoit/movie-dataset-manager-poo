class Catalogo:
    def __init__(self):
        self.filmes = []

    def adicionar_filme(self, filme):
        self.filmes.append(filme)

    def listar_filmes(self):
        for filme in self.filmes:
            print(filme.exibir())

    def buscar_por_titulo(self, titulo):
        for filme in self.filmes:
            if filme.titulo.lower() == titulo.lower():
                return filme
        return None