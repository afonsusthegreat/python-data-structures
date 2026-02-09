def climbstairs(n, memo=None):
    if memo is None:
        memo = {}

    if n <= 1:
        memo[n] == n
        return n
    memo[n] == climbstairs(n-1, memo) + climbstairs(n-2, memo)
    return memo[n]
