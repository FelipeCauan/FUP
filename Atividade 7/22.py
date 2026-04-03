vetor = []
contador = 0

while len(vetor) < 100:
    if contador % 7 != 0 and contador % 10 != 7:
        vetor.append(contador)

    contador += 1

print(vetor)
