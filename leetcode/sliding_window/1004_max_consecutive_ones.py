def maxConsecutiveOnes(nums, k):
    esquerda = 0
    direita = 0
    contagem = {}
    maior_tamanho = 0
    while direita < len(nums):
        tamanho_janela = direita - esquerda + 1
        contagem[nums[direita]] = contagem.get(nums[direita], 0) + 1
        if tamanho_janela - contagem.get(1, 0) <= k:
            maior_tamanho = max(maior_tamanho, tamanho_janela)
        else:
            contagem[nums[esquerda]] -= 1
            esquerda += 1
        direita += 1
    return maior_tamanho
