vetor = []
maior = float('-inf')
menor = float('inf')

for i in range(10):
    vetor.append(int(input()))

for i in range(len(vetor)):
    if vetor[i] > maior:
        maior = vetor[i]
    if vetor[i] < menor:
        menor = vetor[i]

print(maior)
print(menor)
