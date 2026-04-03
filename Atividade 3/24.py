n = int(input())

for i in range(n):
    number = 1

    for j in range(1, i+2):
        print(number, end=" ")
        number = number * (i - j + 1) // j
    print(" ")
