n1 = float(input())
n2 = float(input())
escolha = int(input())

if 1 <= escolha <= 4:

    if escolha == 1:
        media = (n1 + n2) / 2
        print(f"{media:.2f}")

    if escolha == 2:

        if n1 > n2:
            diferenca = n1 - n2
            print(diferenca)
        else:
            diferenca = n2 - n1
            print(diferenca)

    if escolha == 3:
        produto = n1 * n2
        print(f"{produto:.2f}")

    if escolha == 4:

        if n2 != 0:
            divisao = n1/n2
            print(f"{divisao:.2f}")
        else:
            print("Erro")

else:
    print("Erro")
