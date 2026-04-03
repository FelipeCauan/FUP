n = int(input())

if n % 3 == 0 and n % 5 != 0:
    print(True)
elif n % 5 == 0 and n % 3 != 0:
    print(True)
else:
    print(False)
