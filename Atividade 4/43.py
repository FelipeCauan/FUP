idade = 0
maior = 0
menor = 0

while idade >= 0:
    nome = input()
    idade = int(input())

    if idade > 0:
        if idade > maior:
            maior = idade
            velha = nome
        if menor == 0:
            menor = idade
            jovem = nome
        elif idade < menor:
            menor = idade
            jovem = nome
    elif idade < 0:
        break

print(jovem)
print(menor)
print(velha)
print(maior)
