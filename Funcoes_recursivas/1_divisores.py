def conta_divisores(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return conta_divisores_recursiva(n, 1)

def conta_divisores_recursiva(n, divisor_atual):
    if divisor_atual > n:
        return 0
    
    if n % divisor_atual == 0:
        return 1 + conta_divisores_recursiva(n, divisor_atual + 1)
    else:
        return conta_divisores_recursiva(n, divisor_atual + 1)