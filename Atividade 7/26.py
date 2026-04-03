def funcao(x1, x2):
    y = []

    for i in range(len(x1)):
        if x1[i] not in x2:
            y.append(x1[i])

    return y
