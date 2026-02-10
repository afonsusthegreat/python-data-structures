def climb(n):
    if n == 0 or n == 1:
        return 1
    novo = 0
    atual = 1
    anterior = 1
    for i in range(2, n + 1):
        novo = atual + anterior
        anterior = atual
        atual = novo
    return atual
