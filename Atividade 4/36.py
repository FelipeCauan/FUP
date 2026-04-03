def funcao(n):
    maior = 0
    contador = 0

    for i in range(1, n+1):
        if n % i == 0:
            for j in range(1, i):
                if i % j == 0:
                    contador += 1

            if contador <= 1:
                maior = i

        contador = 0

    return maior
