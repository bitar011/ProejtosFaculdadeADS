import matplotlib.pyplot as plt

#Classe que irá representar um livro
class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.titulo} - {self.autor} | Gênero: {self.genero} | Quantidade: {self.quantidade}"


#Lista que representa a biblioteca
biblioteca = []

#---------------------- FUNÇÕES DE GERENCIAMENTO ----------------------

def cadastrar_livro():
    """
    Cadastra um novo livro na biblioteca via input do usuário.
    """
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o gênero do livro: ")
    quantidade = int(input("Digite a quantidade de exemplares: "))

    novo_livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.append(novo_livro)
    print(f"\n📖 Livro '{titulo}' cadastrado com sucesso!\n")


def listar_livros():
    """
    Lista todos os livros da biblioteca.
    """
    if not biblioteca:
        print("\nA biblioteca está vazia.\n")
        return
    print("\n📚 Livros disponíveis na biblioteca:")
    for livro in biblioteca:
        print(livro)


def buscar_livro():
    """
    Busca um livro pelo título informado pelo usuário.
    """
    titulo = input("Digite o título do livro que deseja buscar: ")
    for livro in biblioteca:
        if livro.titulo.lower() == titulo.lower():
            print("\n🔎 Livro encontrado:")
            print(livro)
            return livro
    print(f"\nLivro '{titulo}' não encontrado.")
    return None


def gerar_grafico_por_genero():
    """
    Gera um gráfico de barras mostrando a quantidade de livros por gênero.
    """
    if not biblioteca:
        print("\nNão há livros cadastrados para gerar o gráfico.")
        return
    
    #Contagem de livros por gênero
    generos = {}
    for livro in biblioteca:
        generos[livro.genero] = generos.get(livro.genero, 0) + livro.quantidade
    
    #Preparar dados para o gráfico
    nomes_generos = list(generos.keys())
    quantidades = list(generos.values())
    
    # Criar gráfico
    plt.bar(nomes_generos, quantidades, color='skyblue', edgecolor='black')
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade de Livros")
    plt.title("Quantidade de Livros por Gênero na Biblioteca")
    
    #Adicionar rótulos nas barras
    for i, qtd in enumerate(quantidades):
        plt.text(i, qtd + 0.1, str(qtd), ha='center')
    
    plt.show()


#---------------------- MENU INTERATIVO ----------------------

def menu():
    while True:
        print("\n=== Sistema de Gerenciamento de Biblioteca ===")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Buscar livro pelo título")
        print("4 - Gerar gráfico por gênero")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            buscar_livro()
        elif opcao == "4":
            gerar_grafico_por_genero()
        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")

#Executar o menu
menu()
