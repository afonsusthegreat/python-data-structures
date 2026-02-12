def pot(a, b):
    if b == 0:
        return 1
    atual = 1
    for i in range(1, b + 1):
        atual = a * atual
    return atual
