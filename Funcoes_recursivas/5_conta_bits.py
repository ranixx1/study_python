def conta_bits(n):
    if n == 0:
        return 0
    return 1 + conta_bits(n // 2)
