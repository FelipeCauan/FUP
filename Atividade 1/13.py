num = int(input())

unidade = (num // 1) % 10
dezena = (num // 10) % 10
centena = (num // 100) % 10

novo_num = (unidade*100) + (dezena*10) + centena

print(novo_num)
