def climb(n):
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n+1)  # cria lista com n + 1 elementos
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i+2]
    return dp[n]
