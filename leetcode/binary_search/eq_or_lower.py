def eq_or_lower(nums, alvo):
    esq = 0
    dir = len(nums) - 1
    resposta = -1
    while esq <= dir:
        meio = (esq + dir) // 2
        if nums[meio] <= alvo:
            resposta = meio
            esq = meio + 1
        elif nums[meio] > alvo:
            dir = meio - 1
    return resposta
