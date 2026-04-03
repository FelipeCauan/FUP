vetor = []

for i in range(15):
    vetor.append(int(input()))

contador = 0
for i in range(len(vetor)):
    if vetor[i] % 2 == 0:
        contador += 1
print(contador)

for i in range(len(vetor)):
    if vetor[i] % 2 == 0:
        print(vetor[i])
