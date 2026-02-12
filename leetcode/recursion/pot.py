def pot(a, b, mem=None):
    if mem is None:
        mem = {}

    if b in mem:
        return mem[b]

    if b == 0:
        mem[b] = 1
        return 1

    if b % 2 == 0:
        half = pot(a, b//2, mem)
        mem[b] = half * half
        return mem[b]

    mem[b] = a * pot(a, b-1, mem)
    return mem[b]
