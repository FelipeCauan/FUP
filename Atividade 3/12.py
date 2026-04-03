def funcao(n, k):
    factorialN = 1
    factorialK = 1
    factorialNK = 1

    for i in range(n, 1, -1):
        factorialN = factorialN*i

    for i in range(k, 1, -1):
        factorialK = factorialK*i

    for i in range(n-k, 1, -1):
        factorialNK = factorialNK*i

    result = factorialN/(factorialK*(factorialNK))

    return result
