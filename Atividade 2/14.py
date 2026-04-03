def funcao(i):
    unidade = (i//1) % 10
    dezena = (i//10) % 10
    centena = (i//100) % 10

    num = (unidade*100) + (dezena*10) + (centena*1)

    return num
