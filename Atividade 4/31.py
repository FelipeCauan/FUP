n1 = int(input())
n2 = int(input())
soma = 0
mult = 1

if n2 >= n1:
    for i in range(n1, n2+1):
        if i % 2 == 0:
            soma += i
        else:
            mult *= i
else:
    for i in range(n2, n1+1):
        if i % 2 == 0:
            soma += i
        else:
            mult *= i

print(soma)
print(mult)
