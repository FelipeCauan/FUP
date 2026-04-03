def funcao(data):
    dia, mes, ano = data.split("/")

    if dia.isnumeric() and mes.isnumeric() and ano.isnumeric() and len(ano) == 4:
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

        if dia > 31 or dia < 1 or mes > 12 or mes < 1:
            dia = mes = ano = 0
    else:
        dia = mes = ano = 0

    return dia, mes, ano
