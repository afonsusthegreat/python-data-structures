def longest_substring(string):
    janela = set()
    esquerda = 0
    direita = 0
    maior = 0
    while direita < len(string):
        if string[direita] not in janela:
            janela.add(string[direita])
            direita += 1
            if len(janela) > maior:
                maior = len(janela)
        else:
            janela.remove(string[esquerda])
            esquerda += 1
    return maior
