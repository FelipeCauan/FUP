def funcao(num):
    horas = (num//60)//60
    num = num - (horas*60*60)
    minutos = num//60
    num = num - (minutos*60)
    segundos = num

    return horas, minutos, segundos
