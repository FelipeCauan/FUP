nome = input()
tamanho = []

for letra in nome:
    if letra.isalpha() and letra not in tamanho:
        tamanho.append(letra)

print(len(tamanho))
