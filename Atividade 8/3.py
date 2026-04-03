n = int(input())
matriz = []

for i in range(n):
    linhas = []
    for j in range(n):
        produto = i*j
        linhas.append(produto)
    matriz.append(linhas)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print(" ")
