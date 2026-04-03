n = float(input())
maior = n
menor = n

for i in range(9):
    n = float(input())

    if n > maior:
        maior = n
    elif n < menor:
        menor = n

print(f"{menor:.2f}")
print(f"{maior:.2f}")
