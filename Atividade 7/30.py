def funcao(x):
    tamanho = len(x)
    maximo = 0
    inicio1 = -1
    inicio2 = -1

    if tamanho < 2:
        return -1, -1, -1

    for tamanho_seg in range(2, tamanho):
        for i in range(tamanho - tamanho_seg + 1):
            seg1 = x[i:i+tamanho_seg]

            for j in range(i + 1, tamanho - tamanho_seg + 1):
                seg2 = x[j:j + tamanho_seg]

                if seg1 == seg2 and tamanho_seg > maximo:
                    maximo = tamanho_seg
                    inicio1 = i
                    inicio2 = j
                    break

    if maximo == 0:
        return -1, -1, -1
    else:
        return inicio1, inicio2, maximo
