def funcao(n):
    if n == 1:
        return 1
    else:
        soma = 0
        soma += n**3 + (funcao(n - 1))
        return soma
