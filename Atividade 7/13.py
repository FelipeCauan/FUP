import math


def funcao(vetor):
    soma = 0
    contador = 0
    for i in range(len(vetor)):
        soma += vetor[i]

        if vetor[i] < 7.0:
            contador += 1
    media = soma/len(vetor)

    soma = 0
    for i in range(len(vetor)):
        soma += (vetor[i] - media)**2
    desvio = math.sqrt(soma/len(vetor))

    return media, desvio, contador
