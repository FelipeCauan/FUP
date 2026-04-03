numeros = []

for i in range(8):
    numeros.append(float(input()))

x = int(input())
y = int(input())

soma = numeros[x] + numeros[y]
print(f"{soma:.2f}")
