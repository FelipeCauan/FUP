matriz = []

for i in range(4):
    linhas = []
    for j in range(4):
        linhas.append(int(input()))
    matriz.append(linhas)

maior = matriz[0][0]
linha = 0
coluna = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha = i
            coluna = j
    print(" ")

print(linha)
print(coluna)
print(maior)
