def is_anagram(a, b):
    letras_a = {}
    letras_b = {}
    for i in a:
        if i not in letras_a:
            letras_a[i] = 1
        else:
            letras_a[i] += 1
    for i in b:
        if i not in letras_b:
            letras_b[i] = 1
        else:
            letras_b[i] += 1
    return letras_a == letras_b
