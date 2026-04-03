def funcao(data):
    dia, mes, ano = data.split("/")
    dia = int(dia)

    if mes == "01":
        frase = f"{dia} de janeiro de {ano}"
    elif mes == "02":
        frase = f"{dia} de fevereiro de {ano}"
    elif mes == "03":
        frase = f"{dia} de marco de {ano}"
    elif mes == "04":
        frase = f"{dia} de abril de {ano}"
    elif mes == "05":
        frase = f"{dia} de maio de {ano}"
    elif mes == "06":
        frase = f"{dia} de junho de {ano}"
    elif mes == "07":
        frase = f"{dia} de julho de {ano}"
    elif mes == "08":
        frase = f"{dia} de agosto de {ano}"
    elif mes == "09":
        frase = f"{dia} de setembro de {ano}"
    elif mes == "10":
        frase = f"{dia} de outubro de {ano}"
    elif mes == "11":
        frase = f"{dia} de novembro de {ano}"
    elif mes == "12":
        frase = f"{dia} de dezembro de {ano}"

    return frase
