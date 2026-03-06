def best_time_to_buy(prices):
    maior_lucro = 0
    esquerda = 0
    direita = 1
    while direita < len(prices):
        if prices[direita] < prices[esquerda]:
            esquerda = direita
            direita = esquerda + 1
        else:
            if prices[direita] - prices[esquerda] > maior_lucro:
                maior_lucro = prices[direita] - prices[esquerda]
            direita += 1
    return maior_lucro
