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
    
    def filtrar_por_genero(self, genero):
        encontrados = []

        for filme in self.filmes:
            if filme.genero.lower() == genero.lower():
                encontrados.append(filme)
        return encontrados
    
    def ordenar_por_nota(self):
        self.filmes.sort(key=lambda filme: filme.nota, reverse=True)

    def remover_filme(self, titulo):
        for filme in self.filmes:
            if filme.titulo.lower() == titulo.lower():
                self.filmes.remove(filme)
                return True

        return False