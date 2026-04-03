def funcao(n):
    f1 = 1
    f2 = 1
    fn = 1

    for i in range(2, n):
        fn = f1 + f2
        f2 = f1
        f1 = fn

    return fn
