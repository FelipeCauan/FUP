import math

n = float(input())

if n > 0:
    while n > 0:
        quadrado = n**2
        cubo = n**3
        raiz = math.sqrt(n)

        print(f"{quadrado:.2f}")
        print(f"{cubo:.2f}")
        print(f"{raiz:.2f}")

        n = float(input())
