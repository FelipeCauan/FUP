n = int(input())
x = float(input())

menor = x
maior = x

for i in range(n-1):
    x = float(input())

    if x > maior:
        maior = x
    elif x < menor:
        menor = x

print(f"{menor:.2f}")
print(f"{maior:.2f}")
