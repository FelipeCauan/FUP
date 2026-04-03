def funcao(saque):
    notas100 = saque//100
    saque = saque % 100
    notas50 = saque//50
    saque = saque % 50
    notas20 = saque//20
    saque = saque % 20
    notas10 = saque//10
    saque = saque % 10
    notas5 = saque//5
    saque = saque % 5
    notas2 = saque//2
    saque = saque % 2
    moedas = saque//1

    return notas100, notas50, notas20, notas10, notas5, notas2, moedas
