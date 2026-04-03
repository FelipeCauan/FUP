matriz = []

for i in range(4):
    linhas = []
    for j in range(4):
        linhas.append(float(input()))
    matriz.append(linhas)

contador = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > 10:
            contador += 1

print(contador)
