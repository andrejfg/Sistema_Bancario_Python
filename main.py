import click

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3


no = "s"
while no=="s":
    menu = f""""

    Saldo: {saldo}

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    opcao = input(menu)
    try:
        match opcao:
            case "d":
                deposito = int(input("Quanto deseja depositar? "))
                extrato += f"\n{saldo} + {deposito} = {saldo+deposito}"
                saldo = saldo+ deposito
            case "s":
                if numero_saque == LIMITE_SAQUE:
                    print("Quantidade de saques excedidos")
                else:
                    saque = int(input("Quanto deseja sacar? "))

                    if saque < saldo and saque <= limite:
                        extrato += f"\n{saldo} - {saque} = {saldo - saque}"
                        numero_saque +=1
                        saldo -= saque
                    else:
                        print("saque > saldo",saque > saldo)
                        print("saque <= limite",saque <= limite)
                        print("Valor inválido!")
                    print()
            case "e":
                print(extrato)
                print("Saldo:",saldo)
            case "q":
                no = "sair"

    finally:
        if opcao not in ["d","s","e","q"]:
            print("Opção inválida")
        if no != "sair":
            no = input("Nova operação? (s para continuar)")
            no = no.lower()