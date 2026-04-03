def funcao(string, posicoes):
    string_codificada = ""

    for letra in string:
        if letra.isalpha():
            maiuscula = letra.isupper()
            letra = letra.upper()
            n = ord(letra) + posicoes

            if n > ord('Z'):
                n -= 26

            nova_letra = chr(n)

            if not maiuscula:
                nova_letra = nova_letra.lower()

            string_codificada += nova_letra
        else:
            string_codificada += letra

    return string_codificada
