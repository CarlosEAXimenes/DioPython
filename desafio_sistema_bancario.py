menu = """
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Sair
"""
quantidade_saques = 0
saldo = 0
LIMITE_SAQUE = 500
extrato = ""

while True:
    opcao = int(input(menu))
    if (opcao == 1):
        valor_deposito = float(input("Insira o valor do depósito: \n"))
        if(valor_deposito > 0):
            saldo += valor_deposito
            extrato += f"Depósito -> R${valor_deposito:.2f}\n"
        
    elif (opcao == 2):
        if (quantidade_saques < 3):
            valor_saque = float(input("Insira o valor que deseja sacar: \n"))
            
            if(valor_saque < 0):
                print("Valor inserido inválido, tente novamente\n")
                continue
            
            if(valor_saque > saldo):
                print("Não é possivel realizar a operação! Saldo insuficiente\n")
                continue
            
            if(valor_saque > LIMITE_SAQUE):
                print("Valor do saque excede limite de saque permitido\n")
                continue
                
            saldo -= valor_saque
            extrato += f"Saque -> R${valor_saque:.2f}\n"
            quantidade_saques += 1
            print("Saque realizado com sucesso!\n")
        
        else:
            print("Você já excedeu a quantidade de saques permitidas por dia.\n")

        
    elif (opcao == 3):
        print(("Extrato").center(40,"="))
        print(("Não foram realizadas movimentações." if not extrato else extrato).center(40))
        print((f"\nSaldo: R$ {saldo:.2f}").center(40))
        
    
    elif (opcao == 4):
        break
    
    else:
        print("Opção inválida, favor tentar novamente!")
    
