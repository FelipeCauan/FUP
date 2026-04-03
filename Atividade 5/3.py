palavra = input()
caractere = input()
vogais = "AEIOUaeiou"
contador = 0
nova = ""

for i in palavra:
    if i not in vogais:
        nova += i
    else:
        contador += 1
        nova += caractere

print(contador)
print(nova)
