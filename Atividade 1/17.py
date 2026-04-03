aposta1 = float(input("Digite o valor da primeira aposta:"))
aposta2 = float(input("Digite o valor da segunda aposta:"))
aposta3 = float(input("Digite o valor da terceira aposta:"))
premio = float(input("Digite o valor do prêmio:"))

apostaTotal = aposta1 + aposta2 + aposta3
premio1 = (aposta1/apostaTotal) * premio
premio2 = (aposta2/apostaTotal) * premio
premio3 = (aposta3/apostaTotal) * premio

print(f"O primeiro apostador recebe: {premio1:.2f}")
print(f"O segundo apostador recebe: {premio2:.2f}")
print(f"O terceiro apostador recebe: {premio3:.2f}")
