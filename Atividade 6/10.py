def funcao(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        f = 0
        f += 2 * funcao(n - 1) + 3 * funcao(n - 2)
        return f
