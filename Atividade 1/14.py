num = int(input())

unidade = (num // 1) % 10
dezena = (num // 10) % 10
centena = (num // 100) % 10
uni_milhar = (num // 1000) % 10

print(uni_milhar)
print(centena)
print(dezena)
print(unidade)
