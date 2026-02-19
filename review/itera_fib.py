def fib(n):
    if n == 0 or n == 1:
        return n
    atual = 1
    anterior = 0
    novo = 1
    for i in range(2, n+1):
        novo = atual + anterior
        anterior = atual
        atual = novo
    return atual
