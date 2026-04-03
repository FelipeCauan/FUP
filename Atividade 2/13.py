def funcao(premio):
    ganhador1 = premio*(46/100)
    ganhador2 = premio*(32/100)
    ganhador3 = premio - (ganhador1 + ganhador2)

    return ganhador1, ganhador2, ganhador3
