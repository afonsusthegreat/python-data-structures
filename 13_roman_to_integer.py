s = input()
soma = 0
i = 0
while i < len(s):
    if s[i] == 'I':
        if i + 1 < len(s) and s[i + 1] == 'V':
            soma += 4
            i += 1
            i += 1
        elif i + 1 < len(s) and s[i + 1] == 'X':
            soma += 9
            i += 1
            i += 1
        else:
            soma += 1
            i += 1
    elif s[i] == 'X':
        if i + 1 < len(s) and s[i + 1] == 'L':
            soma += 40
            i += 1
            i += 1
        elif i + 1 < len(s) and s[i + 1] == 'C':
            soma += 90
            i += 1
            i += 1
        else:
            soma += 10
            i += 1
    elif s[i] == 'C':
        if i + 1 < len(s) and s[i + 1] == 'D':
            soma += 400
            i += 1
            i += 1
        elif i + 1 < len(s) and s[i + 1] == 'M':
            soma += 900
            i += 1
            i += 1
        else:
            soma += 100
            i += 1
    elif s[i] == 'V':
        soma += 5
        i += 1
    elif s[i] == 'L':
        soma += 50
        i += 1
    elif s[i] == 'D':
        soma += 500
        i += 1
    elif s[i] == 'M':
        soma += 1000
        i += 1
print(soma)
