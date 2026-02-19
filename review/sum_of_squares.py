def sumof(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    else:
        if n == 0 or n == 1:
            memo[n] = n
            return memo[n]
        memo[n] = n**2 + sumof(n-1)
        return memo[n]
