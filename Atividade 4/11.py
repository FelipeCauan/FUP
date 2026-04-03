n1 = float(input())
sinal = input()
n2 = float(input())

if sinal == "+":
    soma = n1 + n2
    print(f"{soma:.2f}")
elif sinal == "-":
    subtracao = n1 - n2
    print(f"{subtracao:.2f}")
elif sinal == "*":
    multiplicao = n1 * n2
    print(f"{multiplicao:.2f}")
elif sinal == "/":
    divisao = n1/n2
    print(f"{divisao:.2f}")
