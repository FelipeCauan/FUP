vetor = []

for i in range(100):
    vetor.append(float(input()))

codigo = 1

while codigo != 0:
    codigo = int(input())

    if codigo == 0:
        break
    elif codigo == 1:
        for i in range(len(vetor)):
            print(f"{vetor[i]:.1f}")

    elif codigo == 2:
        vetorInvertido = vetor[::-1]
        for i in range(len(vetorInvertido)):
            print(f"{vetorInvertido[i]:.1f}")

    else:
        print("Codigo invalido")
