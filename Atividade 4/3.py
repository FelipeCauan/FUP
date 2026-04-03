n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
soma = 0

if n1 % 2 == 0:
    soma += n1
if n2 % 2 == 0:
    soma += n2
if n3 % 2 == 0:
    soma += n3
if n4 % 2 == 0:
    soma += n4

print(soma)
