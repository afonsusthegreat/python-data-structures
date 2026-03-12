def minimumWindowSubstring(string1, string2):
    # string1 é o que a gente tem que encontrar
    contagem1 = {}
    contagem2 = {}
    validos = 0
    for i in string1:
        contagem1[i] = contagem1.get(i, 0) + 1
    esquerda = 0
    direita = 0
    menorString = None
    while direita < len(string2):
        char = string2[direita]
        contagem2[char] = contagem2.get(char, 0) + 1  # só uma vez
        if char in contagem1 and contagem2[char] == contagem1[char]:
            validos += 1
        while validos == len(contagem1):
            janela = string2[esquerda:direita + 1]
            if menorString is None or len(janela) < len(menorString):
                menorString = janela
            char_esq = string2[esquerda]
            if (char_esq in contagem1 and
                    contagem2[char_esq] == contagem1[char_esq]):
                validos -= 1
            contagem2[char_esq] -= 1
            esquerda += 1
        direita += 1
    return menorString


if __name__ == "__main__":
    print(minimumWindowSubstring("ABC", "ADOBECODEBANC"))
