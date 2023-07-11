def depositar(saldo, valor, extrato, /):
    if(valor > 0):
        saldo += valor_deposito
        extrato += f"Depósito -> R${valor_deposito:.2f}\n"
    else:
        print("Não foi possivel realizar o depósito, valor inserido é inválido!")

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if (numero_saques < limite_saques):
            
            if(valor < 0):
                print("Valor inserido inválido, tente novamente\n")
                return
            
            if(valor > saldo):
                print("Não é possivel realizar a operação! Saldo insuficiente\n")
                return
            
            if(valor > limite):
                print("Valor do saque excede limite de saque permitido\n")
                return
                
            saldo -= valor
            extrato += f"Saque -> R${valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!\n")
            return saldo, extrato
 
    else:
        print("Você já excedeu a quantidade de saques permitidas por dia.\n")
        return

def mostrar_extrato(saldo, /, *, extrato):
    print(("Extrato").center(40,"="))
    print(("Não foram realizadas movimentações." if not extrato else extrato).center(40))
    print((f"\nSaldo: R$ {saldo:.2f}").center(40))

def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_usuario(cpf, clientes)

    if cliente:
        print("CPF já cadastrado!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, clientes)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nCPF inserido não encontrado!")


menu = """
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Novo Cliente
    [5] Nova Conta
    [6] Excluir Conta
    [7] Excluir Cliente
    [8] Sair
    
"""
quantidade_saques = 0
saldo = 0
LIMITE_SAQUE = 500

extrato = ""

clientes = []
contas = []
NUMERO_AGENCIA = 0001

while True:
    opcao = int(input(menu))
    if (opcao == 1):
        valor_deposito = float(input("Insira o valor do depósito: \n"))
        depositar(saldo,valor_deposito,extrato)

        
    elif (opcao == 2):
        valor_saque = float(input("Insira o valor que deseja sacar: \n"))
        saldo, extrato = sacar(
                saldo=saldo,
                valor=valor_saque,
                extrato=extrato,
                limite=LIMITE_SAQUE,
                numero_saques=quantidade_saques,
                limite_saques=3,)

    elif (opcao == 3):
        mostrar_extrato(saldo, extrato=extrato)
        
    elif (opcao == 4):
        clientes = criar_cliente()
    
    elif (opcao == 5):
        numero_conta = len(contas)+1
        criar_conta(NUMERO_AGENCIA, numero_conta, clientes)
        
    else:
        print("Opção inválida, favor tentar novamente!")
    
