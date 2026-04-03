soma = 0
media = 0
n = 0.00

for i in range(3):
    n = float(input())

    if 0.00 <= n <= 10.00:
        soma += n
    else:
        print("Nota invalida")
        break

    media = soma/3

    if i == 2:
        print(f"{media:.2f}")
    else:
        continue
