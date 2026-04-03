matriz = []

for i in range(5):
    linhas = []
    for j in range(5):
        linhas.append(float(input()))
    matriz.append(linhas)

somas = []
for i in range(len(matriz)):
    soma = 0
    for j in range(len(matriz[i])):
        soma += matriz[j][i]
    somas.append(int(soma))
print(somas)
