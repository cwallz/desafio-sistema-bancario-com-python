menu = """
========================================
Escolha uma opção:
========================================

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0

limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("OPERAÇÃO REALIZADA COM SUCESSO!")

        else:
            print("OPERAÇÃO FALHOU! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("OPERAÇÃO FALHOU! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("OPERAÇÃO FALHOU! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("OPERAÇÃO FALHOU! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("OPERAÇÃO REALIZADA COM SUCESSO!")

        else:
            print("OPERAÇÃO FALHOU! O valor informado é inválido.")

    elif opcao == "3":
        titulo = "EXTRATO"
        largura_total = 40  
        espaco_titulo = largura_total - 2

        titulo_formatado = f"={titulo.center(espaco_titulo, ' ')}="

        print("\n" + "=" * largura_total)
        print(titulo_formatado)
        print("=" * largura_total)
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=" * largura_total)
        
    elif opcao == "4":
        print("Caso precise de mais alguma coisa, estamos à disposição.\nTenha um ótimo dia!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")