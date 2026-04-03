def funcao(n):
    width = 2 * n - 1

    for i in range(1, n+1):
        num = 2 * i - 1
        spaces = (width - num) // 2
        lines = " " * spaces + "*" * num
        print(lines)
