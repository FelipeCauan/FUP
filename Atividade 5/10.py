def funcao(n1, n2):
    contador = 0
    divisor = 0
    
    if n1 < n2:
        menor = n1
    else:
        menor = n2

    while contador < menor:
        contador += 1
        
        if n1 % contador == 0 and n2 % contador == 0:
            divisor = contador
        
    return divisor
