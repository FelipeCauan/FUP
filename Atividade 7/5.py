numeros = []

for i in range(10):
    numeros.append(float(input()))

quadrados = []
for i in range(len(numeros)):
    n = numeros[i]
    quadrados.append(n**2)

for i in range(len(numeros)):
    print(f"{numeros[i]:.2f}")

for i in range(len(quadrados)):
    print(f"{quadrados[i]:.2f}")
