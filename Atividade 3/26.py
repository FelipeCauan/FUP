import math


def funcao(x, n):
    sin = 0.00

    for i in range(n + 1):
        numer = (-1)**i * x**(2*i + 1)
        denom = math.factorial(2*i + 1)
        amount = numer / denom
        sin = sin + amount

    return sin
