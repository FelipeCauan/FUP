vetor = []

for i in range(10):
    vetor.append(int(input()))

for i in range(10):
    for j in range(i + 1, 10):
        if vetor[i] == vetor[j]:
            print(vetor[i])
