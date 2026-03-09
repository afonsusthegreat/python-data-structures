def min_size_subarray_sum(target, nums):
    esquerda = 0
    direita = 0
    menor_tamanho = float('inf')
    soma = 0
    while direita < len(nums):
        soma += nums[direita]
        while soma >= target:
            menor_tamanho = min(menor_tamanho, direita - esquerda + 1)
            soma -= nums[esquerda]
            esquerda += 1
        direita += 1
    return 0 if menor_tamanho == float('inf') else menor_tamanho
