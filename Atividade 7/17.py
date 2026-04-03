def funcao(x, n):
    multiplos = []
    for i in range(len(x)):
        if x[i] % n == 0:
            multiplos.append(x[i])

    return multiplos
