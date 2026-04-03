def funcao(x):
    y = []

    for i in range(len(x)):
        contador = 0

        for j in range(len(x)):
            if x[i] == x[j]:
                contador += 1

        if contador == 1:
            y.append(x[i])

    return y
