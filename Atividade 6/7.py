def funcao(n):
    if n % 2 != 0:
        return 0
    elif n == 0:
        print(0)
    else:
        funcao(n - 2)
        print(n)
