import math

a = float(input())
b = float(input())
c = float(input())

if a != 0:
    delta = b**2 - (4*a*c)

    if delta > 0:
        raiz = math.sqrt(delta)
        x1 = (-b + raiz) / (2 * a)
        x2 = (-b - raiz) / (2 * a)

        print(f"{x1:.2f}")
        print(f"{x2:.2f}")

    elif delta == 0:
        raiz = math.sqrt(delta)
        x = (-b + raiz) / (2 * a)

        print(f"{x:.2f}")
        print("Raiz unica")

    else:
        print("Nao existe raiz real")

else:
    print("Nao eh equacao do 2o grau")
