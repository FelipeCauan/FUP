for i in range(1000, 9999+1):
    algarismos1 = i//100
    algarismos2 = i % 100
    soma = algarismos1 + algarismos2

    if soma**2 == i:
        print(i)
