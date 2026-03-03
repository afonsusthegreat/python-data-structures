def max_avg_subarray(nums, k):
    esquerda = 0
    direita = k
    soma_atual = sum(nums[0:k])
    maior_soma = soma_atual
    while direita < len(nums):
        soma_atual = soma_atual - nums[esquerda] + nums[direita]
        if soma_atual > maior_soma:
            maior_soma = soma_atual
        direita += 1
        esquerda += 1
    return maior_soma / k
