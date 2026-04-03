matriz = []

for i in range(5):
    linhas = []
    for j in range(5):
        linhas.append(int(input()))
    matriz.append(linhas)

x = int(input())
linha = 0
coluna = 0
existe = False

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == x:
            existe = True
            linha = i
            coluna = j
            break
    if existe == True:
        break

if existe == True:
    print(linha)
    print(coluna)
else:
    print("Nao encontrado")
