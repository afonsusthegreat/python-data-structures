def paths(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        return (paths(m-1, n) + paths(m, n-1))


print(paths(3, 3))  # VAMO CARALHOOOOOOOOOO
