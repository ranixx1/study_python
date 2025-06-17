def primo(n):
    if n <=1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
def checa_primo_recursivo(n, divisor_atual):
    if divisor_atual > n // 2:
        return True
    
    if n % divisor_atual == 0:
        return False

    return checa_primo_recursivo(n, divisor_atual + 2)