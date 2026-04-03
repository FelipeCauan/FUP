n1 = int(input())
n2 = int(input())
n3 = int(input())
maior = 0
meio = 0
menor = 0

if n1 > n2:
    if n2 > n3:
        maior = n1
        meio = n2
        menor = n3
    elif n1 > n3:
        maior = n1
        meio = n3
        menor = n2
    else:
        maior = n3
        meio = n1
        menor = n2
elif n2 > n3:
    if n3 > n1:
        maior = n2
        meio = n3
        menor = n1
    else:
        maior = n2
        meio = n1
        menor = n3
else:
    maior = n3
    meio = n2
    menor = n1

print(menor)
print(meio)
print(maior)
