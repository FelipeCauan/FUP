def funcao(aposta1, aposta2, aposta3, premio):
    apostaTotal = aposta1 + aposta2 + aposta3
    apostador1 = premio*(aposta1/apostaTotal)
    apostador2 = premio*(aposta2/apostaTotal)
    apostador3 = premio*(aposta3/apostaTotal)

    return apostador1, apostador2, apostador3
