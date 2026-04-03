n = int(input())
matriz = []

for i in range(n):
    linhas = []
    for j in range(n):
        if i == j:
            linhas.append(1)
        else:
            linhas.append(0)
    matriz.append(linhas)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print(" ")
