print("Seja bem vindo ao nosso banco! ")

menu = '''
Escolha uma das opções abaixo:

[d] Deposito
[s] Saque
[e] Extrato
[q] Sair
      
=>'''

saldo = 0
limite =  500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
      valor = float(input("\nInforme o valor a ser depositado: "))

      if valor > 0:
         saldo += valor
         extrato += f"Deposito: R$ {valor:.2f}\n"
         print("\nSaldo atual: R$" + str(saldo))
      else:
         print("\nO valor informado é invalido")

    elif opcao == "s":
        valor = float(input("\nInforme o valor que deseja sacar: "))
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
           print("\nO valor solicitado é maior que o saldo disponivel! " )
           print(f"\nSaldo atual: R$ {saldo:.2f}")

        elif excedeu_limite:
           print(f"\nO valor solicitado excede o limite: R$ {limite:.2f}")

        elif excedeu_saques:
           print(f"\nVocê excedeu o seu limite de saques diários: {LIMITE_SAQUES}")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\nSaque realizado com sucesso! ")
            print(f"\nSaldo restante: R$ {saldo:.2f}")

        else:
           print("\nO valor informado é invalido!")
           print("\nTente novamente.")
             
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("\nObrigado pela preferência, tenha um ótimo dia!")
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")

        
    



        