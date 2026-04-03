salario = float(input())
valor = float(input())

percentual = salario * (20/100)

if valor > percentual:
    print("Emprestimo nao concedido")
else:
    print("Emprestimo concedido")
