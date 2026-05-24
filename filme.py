class Filme:
    def __init__(self, titulo, ano, genero, diretor, nota):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.diretor = diretor
        self.nota = nota

    def exibir(self):
        return f"{self.titulo} ({self.ano}) - {self.genero} - Nota: {self.nota}"