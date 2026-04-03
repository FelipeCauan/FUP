def SomaSerie(i, j, k):
    if i >= j+1:
        return 0
    else:
        soma = 0
        soma += i + SomaSerie(i + k, j, k)
        return soma
