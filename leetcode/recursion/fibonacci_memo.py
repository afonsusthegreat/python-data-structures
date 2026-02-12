def fibonnaci(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    else:
        if n <= 1:
            memo[n] = n
            return n
        memo[n] = fibonnaci(n-1, memo) + fibonnaci(n-2, memo)
        return memo[n]
