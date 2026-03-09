def longest_repeating_char_replacement(k, string):
    contagem = {}
    esquerda = 0
    direita = 0
    maior_tamanho = 0
    while direita < len(string):
        tamanho_janela = direita - esquerda + 1
        contagem[string[direita]] = contagem.get(string[direita], 0) + 1
        if tamanho_janela - k <= max(contagem.values()):
            maior_tamanho = max(maior_tamanho, tamanho_janela)
        else:
            contagem[string[esquerda]] -= 1
            esquerda += 1
        direita += 1
    return maior_tamanho
