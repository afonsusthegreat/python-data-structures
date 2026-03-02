def valid_palindrome(string):
    esquerda = 0
    direita = len(string) - 1
    while esquerda <= direita:
        if not (string[esquerda].isalnum()):
            esquerda += 1
        elif not (string[direita].isalnum()):
            direita -= 1
        else:
            if string[esquerda].lower != string[direita].lower:
                return False
            else:
                esquerda += 1
                direita -= 1
    return True
