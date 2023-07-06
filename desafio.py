menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3


while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"\nSaldo: R$ {saldo:.2f}")

        else:
            print("Operação falhou! O valor é inválido.")
    
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite
        
        excedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! O saldo insuficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O limite de valor de saque foi excedido.")
       
        elif excedeu_saque:
            print("Operação falhou! O número de saque foi excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
            print(f"\nSaques realizados: {numero_saque}")
            print(f"\nSaldo: R$ {saldo:.2f}")
        else:
            print("Operação falhou! O valor é inválido.")
    
    
    elif opcao == "e":
        print("\n======================= Extrato ===================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n===================================================")

    
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada. ")

