def matrizes():
    matriz = []

    for i in range(4):
        linhas = []
        for j in range(5):
            linhas.append(int(input()))
        matriz.append(linhas)

    return matriz


A = matrizes()
B = matrizes()

C = []
for i in range(4):
    linhas = []
    for j in range(5):
        soma = A[i][j] + B[i][j]
        linhas.append(soma)
    C.append(linhas)

for i in range(len(C)):
    for j in range(len(C[i])):
        print(C[i][j], end=" ")
    print(" ")
