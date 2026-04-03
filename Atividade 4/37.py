def simplificar(num, denom):
    if num < denom:
        menor = num
    else:
        menor = denom

    for i in range(1, menor+1):
        if num % i == 0:
            if denom % i == 0:
                simp1 = num / i
                simp2 = denom / i

    simp1 = int(simp1)
    simp2 = int(simp2)
    return simp1, simp2
