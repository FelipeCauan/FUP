def funcao(n):
    result = 0
    h = 0.00

    for i in range(0, n):
        result = 1/(i+1)
        h = h + result

    return h
