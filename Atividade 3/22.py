n = int(input())
number = 0

for i in range(1, n+1):
    for j in range(i):
        number = number + 1
        print(number, end=" ")

    print(" ")
