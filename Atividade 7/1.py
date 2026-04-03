def funcao(data):
    dia, mes, ano = data.split("/")
    dia = int(dia)
    mes = int(mes)
    
    meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    frase = f"{dia} de {meses[mes - 1]} de {ano}"
    return frase
    