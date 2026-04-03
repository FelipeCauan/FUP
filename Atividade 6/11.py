def mdc(x, y):
    if y == 0:
        return x
    else:
        divisor = mdc(y, x % y)
        return divisor
