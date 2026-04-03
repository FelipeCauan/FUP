lista = []
contador = 0
opcao = "S"

while contador < 5:
    if opcao == "S":
        contador += 1
        lista.append(input("Aluno: "))

        if contador < 5:
            opcao = input("Deseja inserir novo aluno? [S/N] ")
    elif opcao == "N":
        break

nome = input("Aluno para pesquisa: ")

for i in range(contador):
    if nome in lista[i]:
        print(lista[i])
        print(i)
