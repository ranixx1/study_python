def primo(n, k=2):
    if n < 2:
        return False
    if k * k > n:
        return True
    if n % k == 0:
        return False
    return primo(n, k + 1)

def primos(lista):
    if not lista:
        return []
    return ([lista[0]] if primo(lista[0]) else []) + primos(lista[1:])
