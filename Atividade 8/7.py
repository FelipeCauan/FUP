A = []

for i in range(10):
    linhas = []
    for j in range(10):
        if i < j:
            linhas.append(2 * i + 7 * j - 2)
        elif i == j:
            linhas.append(3 * i**2 - 1)
        elif i > j:
            linhas.append(4 * i**3 - 5 * j**2 + 1)
    A.append(linhas)

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=" ")
    print(" ")
