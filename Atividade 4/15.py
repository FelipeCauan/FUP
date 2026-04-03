n = int(input())
contador = 1
soma = 0

while contador < n:

    if n % contador == 0:
        soma += contador

    contador += 1

print(soma)
