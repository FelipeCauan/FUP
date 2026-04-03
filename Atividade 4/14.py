opcao = 0

while opcao != 5:
    print("1 - Adicao \n2 - Subtracao \n3 - Multiplicacao \n4 - Divisao \n5 - Saida ")

    opcao = int(input())

    if opcao == 1:
        n1 = float(input())
        n2 = float(input())
        soma = n1 + n2

        print(f"{soma:.2f}")

    elif opcao == 2:
        n1 = float(input())
        n2 = float(input())
        sub = n1 - n2

        print(f"{sub:.2f}")

    elif opcao == 3:
        n1 = float(input())
        n2 = float(input())
        mult = n1 * n2

        print(f"{mult:.2f}")

    elif opcao == 4:
        n1 = float(input())
        n2 = float(input())
        divisao = n1/n2

        print(f"{divisao:.2f}")
