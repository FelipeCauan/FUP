def funcao(x1, x2):
    y = []

    for i in range(len(x1)):
        if x1[i] not in y:
            y.append(x1[i])

    for i in range(len(x2)):
        if x2[i] not in y:
            y.append(x2[i])

    return y
