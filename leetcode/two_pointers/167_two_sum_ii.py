def two_sum(nums, target):
    esquerda = 0
    direita = len(nums) - 1
    while esquerda < direita:
        soma = nums[esquerda] + nums[direita]
        if soma == target:
            return [esquerda, direita]
        if soma < target:
            esquerda = esquerda + 1
        if soma > target:  # podia usar else, mas deixei assim por clareza
            direita = direita - 1
    return -1  # se não tiver encontrado
