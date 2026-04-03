matriz = []

for i in range(4):
    linhas = []
    for j in range(4):
        linhas.append(int(input()))
    matriz.append(linhas)

transposta = []
for i in range(len(matriz)):
    linhas = []
    for j in range(4):
        linhas.append(matriz[j][i])
    transposta.append(linhas)

for i in range(len(transposta)):
    for j in range(len(transposta[i])):
        print(transposta[i][j], end=" ")
    print(" ")
