import math

raio = float(input("Digite o valor do raio:"))
volume = (4/3) * math.pi * (raio**3)
area = 4 * math.pi * (raio**2)

print(f"O volume da esfera é: {volume:.2f}")
print(f"A área da superfície é: {area:.2f}")
