def trib(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    else:
        if n == 0 or n == 1:
            memo[n] = n
            return n
        if n == 2:
            memo[n] = 1
            return 1
        memo[n] = trib(n-1, memo) + trib(n-2, memo) + trib(n-3, memo)
        return memo[n]
