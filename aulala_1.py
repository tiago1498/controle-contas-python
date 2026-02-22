biblioteca = {}
escolha = 1

def menu():
    print()
    print('1 - Cadastrar livro')
    print('2 - Emprestar ')
    print('3 - Devolver')
    print('4 - Listar')
    print('5 - Encerrar')


def cadastro(biblioteca):
    livro = input('Digite o nome do livro: ').strip()

    if not livro:
        print('Digite um nome válido')
        return biblioteca

    quantidade = int(input('Digite a quantidade: '))

    if quantidade  <=0:
        print('A quantidade deve ser maior que 0')
        return biblioteca

    if livro in biblioteca:
        biblioteca[livro] += quantidade

    else:
        biblioteca[livro] = quantidade


    return biblioteca

def emprestar(biblioteca):
    if not biblioteca:
        print('Sem livros para emprestar no momento')
        return biblioteca

    nome_livro = input('Digite o nome do livro: ')

    if not nome_livro in biblioteca:
        print('No momento nao possuimos esse título')
        return biblioteca

    quantidade_emp = int(input('Digite a quantidade '))


    if quantidade_emp <= 0:
        print('A quantidade deve ser maior que 0')
        return biblioteca

    if quantidade_emp > biblioteca[nome_livro]:
        print('Quantidade acima do estoque')
        return biblioteca

    biblioteca[nome_livro] -= quantidade_emp


def devolucao(biblioteca):
    if not biblioteca:
        print('Sem livros cadastrado no momento')
        return biblioteca
    
    livro_dev = input('Digite o nome do livro: ').strip()

    if not livro_dev:
        print('Digite um nome válido')
        return biblioteca
    
    quantidade_dev = int(input('Digite a quantidade: '))
    
    if quantidade_dev <= 0:
        print('A quantidade deve ser maior que 0')
        return biblioteca
    
    if not livro_dev in biblioteca:
        biblioteca[livro_dev] = quantidade_dev
        return biblioteca
    else:
        biblioteca[livro_dev] += quantidade_dev


def listar(biblioteca):
    for livros in biblioteca:
        print('Título',livros,':',biblioteca[livros])

    
while escolha != 5:
    menu()
    escolha = int(input('Escolha uma opçao: '))

    if escolha == 1:
        cadastro(biblioteca)

    elif escolha == 2:
        emprestar(biblioteca)

    elif escolha == 3:
        devolucao(biblioteca)

    elif escolha == 4:
        listar(biblioteca)

    elif escolha == 5:
        print('Encerrando sistema')

    else:
        print('Opção inválida')
        