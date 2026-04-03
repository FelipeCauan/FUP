import random

n = int(input())
m = int(input())
random.seed(int(input()))
intervalo1 = int(input())
intervalo2 = int(input())

matriz = []
for i in range(n):
    linhas = []
    for j in range(m):
        linhas.append(random.randint(intervalo1, intervalo2))
    matriz.append(linhas)

for i in range(n):
    for j in range(m):
        print(matriz[i][j], end=" ")
    print()

for i in range(n):
    soma = []
    contador = 0
    for j in range(m):
        if i % 2 == 0:
            soma.append(matriz[i][j])
        else:
            if matriz[i][j] % 3 == 0 and matriz[i][j] < 0:
                contador += 1
    if i % 2 == 0:
        print(f'{sum(soma)/len(soma):.2f}')
    else:
        print(contador)
