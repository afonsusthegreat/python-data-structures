def busca(nums, alvo):
    esq = 0
    dir = len(nums) - 1
    while esq <= dir:
        meio = (esq + dir) // 2

        if nums[meio] == alvo:
            return meio
        elif nums[meio] < alvo:
            esq = meio + 1
        elif nums[meio] > alvo:
            dir = meio - 1
    return -1
