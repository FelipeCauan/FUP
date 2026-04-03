contador = 0
soma = 0

while contador < 1000:
    if contador % 3 == 0 or contador % 5 == 0:
        soma += contador
    contador += 1

print(soma)
