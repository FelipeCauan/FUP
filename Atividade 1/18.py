valor = float(input("Digite o valor do saque:"))

notas100 = valor//100
valor = valor % 100
notas50 = valor//50
valor = valor % 50
notas20 = valor//20
valor = valor % 20
notas10 = valor//10
valor = valor % 10
notas5 = valor//5
valor = valor % 5
notas2 = valor//2
valor = valor % 2
moeda = valor

print(f"Notas de 100: {notas100:.0f}")
print(f"Notas de 50: {notas50:.0f}")
print(f"Notas de 20: {notas20:.0f}")
print(f"Notas de 10: {notas10:.0f}")
print(f"Notas de 5: {notas5:.0f}")
print(f"Notas de 2: {notas2:.0f}")
print(f"Moedas de 1 real: {moeda:.0f}")
