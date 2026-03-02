def move_zeroes(lista):
    esquerda = 0
    direita = 0
    while direita < len(lista):
        if lista[direita] != 0:
            lista[esquerda], lista[direita] = lista[direita], lista[esquerda]
            esquerda += 1
            direita += 1
        else:
            direita += 1
    return lista


if __name__ == "__main__":
    print(move_zeroes([0, 1, 0, 3, 12]))
