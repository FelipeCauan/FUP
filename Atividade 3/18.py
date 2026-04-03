def funcao(p):
    factorial = 1
    amount = 0

    for i in range(p, 0, -1):
        factorial = factorial * i

    for i in range(p):
        amount = amount + (factorial % 10)
        factorial = factorial // 10

    return amount
