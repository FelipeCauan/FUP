def funcao(n1, n2):
    contador = 0
    fim = n1 * n2

    while contador < fim:
        contador += 1

        if contador % n1 == 0 and contador % n2 == 0:
            break

    return contador
