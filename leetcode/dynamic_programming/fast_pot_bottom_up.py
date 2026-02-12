def fast_pot(a, b):
    atual = 1
    if b == 0:
        return 1
    while b > 0:
        if b % 2 != 0:
            atual = a * atual
        a = a * a
        b = b // 2
    return atual
