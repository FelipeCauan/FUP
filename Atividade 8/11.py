matriz = []
soma = 0

for i in range(4):
    linhas = []
    for j in range(4):
        linhas.append(int(input()))
    linhasInvertida = linhas[::-1]
    matriz.append(linhasInvertida)
    soma += matriz[i][i]
print(soma)
