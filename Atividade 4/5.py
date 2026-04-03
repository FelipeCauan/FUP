import math

n = float(input())

if n > 0:
    resultado = math.sqrt(n)
    print(f"{resultado:.2f}")
else:
    print("Numero invalido")
