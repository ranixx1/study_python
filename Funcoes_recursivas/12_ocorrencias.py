def ocorrencias(lista, x):
    if not lista:
        return 0
    return (lista[0] == x) + ocorrencias(lista[1:], x)
