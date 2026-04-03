n = int(input())

if n >= 0:
    maior = n
    menor = n

    while n >= 0:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

        n = int(input())

    print(maior)
    print(menor)
