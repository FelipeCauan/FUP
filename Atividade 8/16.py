matriz = []

for i in range(12):
    linhas = []
    for j in range(13):
        linhas.append(float(input()))
    matriz.append(linhas)

matrizResultante = []
for i in range(len(matriz)):
    maior = 0
    for j in range(len(matriz[i])):
        if matriz[i][j] < 0:
            modulo = matriz[i][j] - matriz[i][j] * 2
            if modulo > maior:
                maior = modulo
        elif matriz[i][j] > 0:
            if matriz[i][j] > maior:
                maior = matriz[i][j]

    linhas = []
    for j in range(len(matriz[i])):
        resultado = matriz[i][j]/maior
        linhas.append(resultado)
    matrizResultante.append(linhas)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"{matriz[i][j]:.2f}", end=" ")
    print()
print()
for i in range(len(matrizResultante)):
    for j in range(len(matrizResultante[i])):
        print(f"{matrizResultante[i][j]:.2f}", end=" ")
    print()
