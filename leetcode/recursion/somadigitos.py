def soma_digitos(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n < 10:
        memo[n] = n
        return n

    memo[n] = soma_digitos(n // 10, memo) + soma_digitos(n % 10, memo)
    # n // 10 é divisão sem resto, n % 10 é o resto
    return memo[n]
