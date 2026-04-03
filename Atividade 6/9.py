import math


def sf(n):
    if n == 0:
        return 1
    else:
        superf = 0
        superf += math.factorial(n) * sf(n - 1)
        return superf
