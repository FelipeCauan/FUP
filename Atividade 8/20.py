matriz = []
for i in range(20):
    linhas = []
    for j in range(20):
        linhas.append(int(input()))
    matriz.append(linhas)

maior = float('-inf')
for i in range(20):
    for j in range(17):
        n = matriz[j - 1][i] * matriz[j][i] * \
            matriz[j + 1][i] * matriz[j + 2][i]
        if n > maior:
            maior = n
            x = j - 1
            y = i
            direcao = "baixo"

        n2 = matriz[i][j-1] * matriz[i][j] * matriz[i][j+1] * matriz[i][j+2]
        if n2 > maior:
            maior = n2
            x = i
            y = j-1
            direcao = "direita"

for i in range(17):
    for j in range(17):
        n = matriz[i-1][j-1] * matriz[i][j] * \
            matriz[i+1][j+1] * matriz[i+2][j+2]
        if n > maior:
            maior = n
            x = i-1
            y = j-1
            direcao = "direita baixo"

for i in range(17):
    for j in range(3, 20):
        n = matriz[i][j] * matriz[i+1][j-1] * \
            matriz[i + 2][j - 2] * matriz[i + 3][j - 3]
        if n > maior:
            maior = n
            x = i
            y = j
            direcao = "esquerda baixo"

print(maior)
print(x)
print(y)
print(direcao)
