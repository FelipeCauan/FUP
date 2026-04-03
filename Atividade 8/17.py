def imprimirMatriz(matriz):
    for i in range(12):
        for j in range(13):
            print(f'{matriz[i][j]:.2f}', end=' ')
        print()
    print()


def primo(n):
    contador = 0
    for i in range(2, n):
        if n % i == 0:
            contador += 1
    if contador != 0 or n == 0:
        return False
    else:
        return True


matriz = []
for i in range(12):
    linhas = []
    for j in range(13):
        linhas.append(int(input()))
    matriz.append(linhas)

matrizResultante = []
for i in range(13):
    linhas = []
    maior = float('-inf')
    menor = float('inf')
    teste = float('-inf')
    for j in range(12):
        if matriz[j][i] > maior and primo(abs(matriz[j][i])) == True:
            maior = matriz[j][i]

        if matriz[j][i] < menor:
            menor = matriz[j][i]
    if maior != teste:
        for j in range(12):
            linhas.append(matriz[j][i]/maior)
    else:
        for j in range(12):
            linhas.append(matriz[j][i]/menor)
    matrizResultante.append(linhas)

matrizFinal = []
for i in range(12):
    linhas = []
    for j in range(13):
        linhas.append(matrizResultante[j][i])
    matrizFinal.append(linhas)

imprimirMatriz(matriz)
imprimirMatriz(matrizFinal)
