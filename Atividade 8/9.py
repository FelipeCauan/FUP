matriz = []

for i in range(4):
    linhas = []
    for j in range(4):
        linhas.append(int(input()))
    matriz.append(linhas)

soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if j < i:
            soma += matriz[i][j]
print(soma)
