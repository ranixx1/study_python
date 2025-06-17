def soma_pares(lista):
    if not lista:
        return 0
    return (lista[0] if lista[0] % 2 == 0 else 0) + soma_pares(lista[1:])
