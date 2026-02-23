def floor_raiz_inteira(n):
    esq = 0
    dir = n
    resposta = 0
    while esq <= dir:
        meio = (esq + dir) // 2
        if meio**2 <= n:
            """pode substituir por meio <= n // meio
            para evitar overflow"""
            resposta = meio
            esq = meio + 1

        else:
            dir = meio - 1
    return resposta
