import textwrap

def menu():
    print("Seja bem vindo ao nosso banco!")
    menu = '''\n
    Escolha uma das opções abaixo:

    [d] \tDeposito
    [s] \tSaque
    [e] \tExtrato
    [nc] \tNova conta
    [lc] \tListar contas
    [nu] \tNovo usuário
    [q] \tSair    
    =>'''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n==== Depósito Realizado! ====")
    else:
        print("\n!!! A operação falhou, valor inválido !!!")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nSaldo Insuficiente")
    elif excedeu_limite:
        print("\nO valor desejado excede o limite")
    elif excedeu_saques:
        print("\nVocê atingiu o número máximo de saques, tente novamente amanhã")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n==== Saque Realizado! ====")
    else:
        print("\n!!! A operação falhou, valor inválido !!!")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n====== Extrato ======")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nO CPF já existe na base!")
        return

    nome = input("\nInforme o seu nome: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço (rua, número - bairro - cidade/sigla do estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n### Usuário criado ###")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta Criada! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência: \t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("\nInforme o valor a ser depositado: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("\nInforme o valor que deseja sacar: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("\nObrigado pela preferência, tenha um ótimo dia!")
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

main()
