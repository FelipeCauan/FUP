import random

matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
jogadores = ['humano', 'maquina']
jogador = random.choice(jogadores)
fim = False
contador = 0


def tabuleiro():
    for i in range(3):
        print(f' {matriz[i][0]} | {matriz[i][1]} | {matriz[i][2]} ')
        if i <= 1:
            print("---+---+---")
    print()


def jogada(jogador):
    global contador

    if jogador == 'humano':
        while True:
            linha = int(input("Escolha a linha que deseja jogar: "))-1
            coluna = int(input("Escolha a coluna que deseja jogar: "))-1

            if linha > -1 and linha < 3 and coluna > -1 and coluna < 3 and matriz[linha][coluna] == ' ':
                matriz[linha][coluna] = 'X'
                contador += 1
                tabuleiro()
                break
            else:
                print("Jogada inválida.")
    else:
        while True:
            linha, coluna = random.randint(0, 2), random.randint(0, 2)
            if matriz[linha][coluna] == ' ':
                matriz[linha][coluna] = 'O'
                contador += 1
                tabuleiro()
                break


def vencedor():
    resultado = False
    for sinal in 'XO':
        if resultado == True:
            break

        for i in range(3):
            if resultado == False and matriz[i][0] == matriz[i][1] and matriz[i][1] == matriz[i][2] and matriz[i][0] == sinal:
                resultado = True
                if sinal == 'X':
                    print("Jogador venceu!")
                    break
                else:
                    print("Máquina venceu!")
                    break
        for i in range(3):
            if resultado == False and matriz[0][i] == matriz[1][i] and matriz[1][i] == matriz[2][i] and matriz[0][i] == sinal:
                resultado = True
                if sinal == 'X':
                    print("Jogador venceu!")
                    break
                else:
                    print("Máquina venceu!")
                    break
        if resultado == False and matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2] and matriz[0][0] == sinal:
            resultado = True
            if sinal == 'X':
                print("Jogador venceu!")
                break
            else:
                print("Máquina venceu!")
                break
        elif resultado == False and matriz[0][2] == matriz[1][1] and matriz[1][1] == matriz[2][0] and matriz[0][2] == sinal:
            resultado = True
            if sinal == 'X':
                print("Jogador venceu!")
                break
            else:
                print("Máquina venceu!")
                break
    if resultado == False and contador > 8:
        print("Empate!")
        resultado = True

    return resultado


if jogador == 'humano':
    ordem = ['humano', 'maquina']
if jogador == 'maquina':
    ordem = ['maquina', 'humano']

tabuleiro()

while True:
    for i in ordem:
        jogada(i)
        if vencedor() == True:
            fim = True
            break
    if fim == True:
        break
