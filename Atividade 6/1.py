def funcao(n):
    if n == 0:
        return 0
    else:
        soma = 0
        soma += n + funcao(n - 1)
        return soma
