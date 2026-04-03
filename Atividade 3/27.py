def funcao(n):
    exp = n - 1

    for i in range(2, n):
        exp = exp**(n - i)

    result = n**exp
    return result
