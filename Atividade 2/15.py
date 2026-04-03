def funcao(i):
    uni_Milhar = (i//1000) % 10
    centena = (i//100) % 10
    dezena = (i//10) % 10
    unidade = (i//1) % 10

    return uni_Milhar, centena, dezena, unidade
