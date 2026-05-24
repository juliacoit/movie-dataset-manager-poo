from catalogo import Catalogo
from filme import Filme
from persistencia import carregar_filmes, salvar_filmes

CAMINHO = "filmes.csv"

catalogo = Catalogo()

filmes_carregados = carregar_filmes(CAMINHO)
for filme in filmes_carregados:
    catalogo.adicionar_filme(filme)


def mostrar_menu():
    print("\n===== CATÁLOGO DE FILMES =====")
    print("1 - Listar filmes")
    print("2 - Buscar filme por título")
    print("3 - Adicionar filme")
    print("4 - Remover Filme")
    print("5 - Filtrar por gênero")
    print("6 - Ordenar por nota")
    print("7 - Salvar alterações")
    print("0 - Sair")


while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        catalogo.listar_filmes()

    elif opcao == "2":
        titulo = input("Digite o título do filme: ")
        filme = catalogo.buscar_por_titulo(titulo)

        if filme:
            print("\nFilme encontrado:")
            print(filme.exibir())
        else:
            print("Filme não encontrado.")

    elif opcao == "3":
        titulo = input("Título: ")
        ano = int(input("Ano: "))
        genero = input("Gênero: ")
        diretor = input("Diretor: ")
        nota = float(input("Nota: "))

        novo_filme = Filme(titulo, ano, genero, diretor, nota)
        catalogo.adicionar_filme(novo_filme)

        print("Filme adicionado com sucesso!")

    elif opcao == "4":
        titulo = input("Digite o título do filme para remover: ")

        removido = catalogo.remover_filme(titulo)

        if removido:
            print("Filme removido com sucesso!")
        else:
            print("Filme não encontrado.")    

    elif opcao == "5":
        genero = input("Digite o gênero: ")

        resultados = catalogo.filtrar_por_genero(genero)

        if resultados:
            print(f"\nFilmes do gênero {genero}:\n")

            for filme in resultados:
                print(filme.exibir())

        else:
            print("Nenhum filme encontrado.")

    elif opcao == "6":
        catalogo.ordenar_por_nota()

        print("\nFilmes ordenados por nota:\n")
        catalogo.listar_filmes()

    elif opcao == "7":
        salvar_filmes(CAMINHO, catalogo.filmes)
        print("Alterações salvas com sucesso!")

    elif opcao == "0":
        salvar = input("Deseja salvar antes de sair? (s/n): ")

        if salvar.lower() == "s":
            salvar_filmes(CAMINHO, catalogo.filmes)
            print("Alterações salvas.")

        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")