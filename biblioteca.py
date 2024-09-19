def crialivro(biblioteca):
    nome = input('informe o nome do livro: ')
    autor = input('informe o nome do autor: ')
    ano = input('informe o ano de lançamento do livro: ')
    livro = [nome, autor, ano]
    biblioteca.append(livro)
    return biblioteca

def imprime(biblioteca):
    if not biblioteca:
        print('A biblioteca está vazia')
    else:
        print(biblioteca)

def buscalivro(biblioteca):
    busca = input('informe o nome do livro que deseja deletar: ')
    for i in range(len(biblioteca)):
        for j in range(3):
            if biblioteca[i][j] == busca:
                print(biblioteca[i])
            else:
                print("Este livro não está na biblioteca")

biblioteca = []
continuar = True
while continuar:
    print('Menu')
    print('1. Adicionar Livro')
    print('2. Listar Livros')
    print('3. Buscar Livro')
    print('4. Sair')
    opcao = int(input("Escolha uma opção: "))
    
    match opcao:
        case 1:
            crialivro(biblioteca)
        case 2:
            imprime(biblioteca)
        case 3:
            buscalivro(biblioteca)
        case 4:
            continuar = False