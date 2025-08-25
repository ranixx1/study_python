def inverter_lista(lista, i=0, j=None):
    if j is None:
        j = len(lista) - 1
    if i >= j:
        return lista
    lista[i], lista[j] = lista[j], lista[i]
    return inverter_lista(lista, i + 1, j - 1)
