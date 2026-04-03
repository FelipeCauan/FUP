def funcao(n):
    amount = 0
    numer = 0
    denom = 0

    for i in range(1, n+1):
        numer = i**2 + 1
        denom = i + 3
        amount = amount + numer/denom

    return amount
