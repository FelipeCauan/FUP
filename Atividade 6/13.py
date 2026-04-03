def A(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        resultado = 0
        resultado += A(m - 1, 1)
        return resultado
    else:
        resultado = 0
        resultado += A(m - 1, A(m, n - 1))
        return resultado
