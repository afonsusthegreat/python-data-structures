def contar(nums, alvo):
    esq = 0
    dir = len(nums) - 1
    menor = 0
    maior = 0
    while esq <= dir:
        meio = (esq + dir) // 2
        if nums[meio] <= alvo:
            menor = meio
            esq = meio + 1
        elif nums[meio] > alvo:
            dir = meio - 1
    esq = 0
    dir = len(nums) - 1
    while esq <= dir:
        meio = (esq + dir) // 2

        if nums[meio] >= alvo:
            maior = meio
            dir = meio - 1
        elif nums[meio] < alvo:
            esq = meio + 1
    return maior - menor + 1
