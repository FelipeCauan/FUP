quantidade = int(input())
n = int(input())

maior = n
contador = 1

for i in range(quantidade-1):
    n = int(input())

    if n == maior:
        contador += 1
    elif n > maior:
        maior = n
        contador = 1

print(maior)
print(contador)
