def matrizes():
    matriz = []

    for i in range(5):
        linhas = []
        for j in range(5):
            linhas.append(int(input()))
        matriz.append(linhas)

    return matriz


A = matrizes()
B = matrizes()
C = []

for i in range(5):
    linhas = []
    for j in range(5):
        produto = 0
        for k in range(5):
            produto += A[i][k] * B[k][j]
        linhas.append(produto)
    C.append(linhas)

for i in range(len(C)):
    for j in range(len(C[i])):
        print(C[i][j], end=" ")
    print(" ")
