frase = input()
invertida = frase[::-1]
frase_invertida = ""

for letra in invertida:
    if letra == "A":
        frase_invertida += "*"
    elif letra == "a":
        frase_invertida += "*"
    else:
        frase_invertida += letra

print(frase_invertida)
