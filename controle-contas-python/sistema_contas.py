contas = {}

def menu():
    print()
    print('='*30)
    print('******* Menu de contas *******')
    print('='*30)
    print('| 1 - Cadastrar conta ')
    print('| 2 - Atualizar valor da conta ')
    print('| 3 - Pagar conta ')
    print('| 4 - Listar contas ')
    print('| 5 - Somar total de contas ')
    print('| 6 - Sair ')
    print('='*30)
    print()

def cadastro(contas):
    nome = input('Digite o nome da conta: ').strip()
    if not nome:
        print('Digite um nome válido')
        return contas
    try:
        valor = float(input('Valor: '))

        if valor <= 0:
            print('Digite um valor acima de 0')
            return contas
    except ValueError:
        print('!'*5,'Digite apenas numeros','!'*5)
        return contas

    if nome in contas:
        contas[nome] += valor
    else:
        contas[nome] = valor
    print(f'Conta de {nome} cadastrada com sucesso!')
    return contas

def atualizar(contas):
    if not contas:
        print('Sem contas cadastrada')
        return contas

    nome_conta = input('Digite o nome da conta: ')

    if not nome_conta in contas:
            print('Conta nao cadastrada')
            return contas
    try:   
        valor_atualizado = float(input('Digite o novo valor da conta: '))

        if valor_atualizado <= 0:
            print('Digite um valor acima de 0')
            return contas
        
    except ValueError:
        print('Digite apenas numeros!!!')
        return contas

        
    contas[nome_conta] = valor_atualizado
    print(f'Conta de {nome_conta} atualizada com sucesso!')
    return contas

def pagar(contas):
    pag_conta= input('Digite o nome da conta: ').strip()

    if not pag_conta:
        print('Espaço vazio tente novamente')
        return contas

    if not pag_conta in contas:
        print('Conta nao cadastrada')
        return contas
    else:
        print('Conta liquidada com sucesso!')
        del contas[pag_conta]
        return contas

def listar(contas):
    if not contas:
        print('Sem contas a serem exibidas')

    for i in contas:
        print(f'Conta: {i} | valor: R$ {contas[i]}')

opcao = 1

def somar (contas):
    if not contas:
        print('Sem contas para somar')
        return contas


    somar = sum(contas.values())
    print(f' O valor total é de $ {somar:.2f}')
    return contas

while opcao != 6:
    menu()
    try:
        opcao = int(input('Escolha uma opçao: \n'))

        if opcao == 1:
            cadastro(contas)

        elif opcao == 2:
            atualizar(contas)

        elif opcao == 3:
            pagar(contas)

        elif opcao == 4:
            listar(contas)

        elif opcao == 5:
            somar(contas)

        elif opcao == 6:
            print('Encerrando sistema')

        else:
            print('Opçao inválida')

    except ValueError:
        print('!!!!! Digite apenas numeros !!!!!')

