string = input()
nova = ""

for caractere in string:
    if caractere == "0":
        nova += "1"
    elif caractere != "0":
        nova += caractere

print(nova)
