import math


def funcao(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma += vetor[i]
    media = soma/len(vetor)

    soma = 0
    for i in range(len(vetor)):
        soma += (vetor[i] - media)**2
    desvio = math.sqrt(soma/len(vetor))

    return media, desvio
