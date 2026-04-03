def funcao(x1, x2):
    y = []

    for i in range(len(x1)):
        contador = 0

        for j in range(len(x2)):
            if x1[i] == x2[j] and x1[i] not in y:
                contador += 1

                if contador == 1:
                    y.append(x1[i])

    return y
