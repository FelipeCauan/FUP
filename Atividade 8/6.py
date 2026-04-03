def matrizes():
    matriz = []

    for i in range(4):
        linhas = []
        for j in range(4):
            linhas.append(int(input()))
        matriz.append(linhas)

    return matriz


matriz1 = matrizes()
matriz2 = matrizes()
matriz3 = []

for i in range(4):
    linhas = []
    for j in range(4):
        if matriz1[i][j] > matriz2[i][j]:
            linhas.append(matriz1[i][j])
        else:
            linhas.append(matriz2[i][j])
    matriz3.append(linhas)

for i in range(len(matriz3)):
    for j in range(len(matriz3[i])):
        print(matriz3[i][j], end=" ")
    print(" ")
