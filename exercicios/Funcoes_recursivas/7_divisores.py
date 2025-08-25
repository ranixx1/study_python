def divisores(n, k=1):
    if k > n:
        return []
    return ([k] if n % k == 0 else []) + divisores(n, k + 1)
