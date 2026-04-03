def funcao(n):
    if n == 0:
        return 1
    else:
        fatorial = 0
        fatorial += n * funcao(n - 1)
        return fatorial
