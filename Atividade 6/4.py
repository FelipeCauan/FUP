def funcao(n, k):
    if k == 0:
        return 1
    else:
        resultado = 0
        resultado += n * funcao(n, k - 1)
        return resultado
