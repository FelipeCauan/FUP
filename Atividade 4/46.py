string1 = input()
invertida = string1[::-1]
string2 = ""
string_invertida = ""

for letra in string1:
    if letra.isalpha():
        string2 += letra

for letra in invertida:
    if letra.isalpha():
        string_invertida += letra

string2 = string2.lower()
string_invertida = string_invertida.lower()

if string2 == string_invertida:
    print(True)
else:
    print(False)
