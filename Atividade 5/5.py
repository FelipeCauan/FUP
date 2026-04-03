a = int(input())
b = int(input())
c = int(input())

if a + b > c and b + c > a and c + a > b:
    if a == b and b == c:
        print("Triangulo equilatero")
    elif a != b and b != c and c != a:
        print("Triangulo escaleno")
    else:
        print("Triangulo isosceles")
else:
    print("Nao triangulo")
