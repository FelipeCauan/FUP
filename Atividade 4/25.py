contador = 0
soma = 0

while contador < 10:
    n = int(input())

    if n > 0:
        contador += 1
        soma += n
        media = soma/10

print(media)
