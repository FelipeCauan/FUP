def funcao(n):
    amount = 0
    e = 1

    for i in range(0, n):
        factorial = 1

        for j in range(i+1, 0, -1):
            factorial = factorial * j

        amount = amount + (1/factorial)

    e = e + amount

    return e
