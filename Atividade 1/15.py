valor = int(input("Digite o valor em segundos:"))

horas = (valor // 60) // 60
minutos = (valor - (horas*60*60)) // 60
segundos = valor - ((horas*60*60) + (minutos*60))

print(f"{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)")
