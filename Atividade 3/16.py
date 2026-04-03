num = 1
den = 1
s = 0

for i in range(0, 99, 2):
    s = s + (num/den)

    num = num + 2
    den = den + 1

print(f"{s:.10f}")
