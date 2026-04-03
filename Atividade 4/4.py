n1 = float(input())
n2 = float(input())
n3 = float(input())
maior = 0

if n1 > n2:
    if n1 > n3:
        maior = n1
    else:
        maior = n3
elif n3 > n2:
    maior = n3
else:
    maior = n2

print(maior)
