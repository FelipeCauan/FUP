n1 = int(input())
n2 = int(input())

if n2 > n1:
    fracao = n1**(-1)
    divisao = n2 * fracao
else:
    fracao = n2**(-1)
    divisao = n1 * fracao

print(int(divisao))
