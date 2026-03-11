def permutationInString(string1, string2):
    contagem1 = {}
    for i in string1:
        contagem1[i] = contagem1.get(i, 0) + 1
    esquerda = 0
    direita = len(string1) - 1
    contagem2 = {}
    for i in range(len(string1)):
        contagem2[string2[i]] = contagem2.get(string2[i], 0) + 1
        """inicializa um dict que será alterado conforme necessário"""
    while direita < len(string2):
        if contagem1 == contagem2:
            return True
        else:
            contagem2[string2[esquerda]] -= 1
            esquerda += 1
            direita += 1
            if direita < len(string2):
                char = string2[direita]
                contagem2[char] = contagem2.get(char, 0) + 1
            """provavelmente tem maneira mais elegante,
                mas isso já garante O(n)"""
    return False
