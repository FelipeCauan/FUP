vetor = []
contador = 0

while contador < 12:
    num = int(input())

    if num not in vetor:
        vetor.append(num)
        contador += 1
    else:
        print(f"Numero {num} ja existe, escreva outro")

print(vetor)
