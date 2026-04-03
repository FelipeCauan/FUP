string = input()
vogais = "AEIOUaeiou"
sem = ""

for i in string:
    if i not in vogais:
        sem += i

print(sem)
