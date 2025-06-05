def lista_troca_menor_primeiro(lista):
    menor_elemento = lista[0]
    indice_menor = 0

    for i in range(1, len(lista)):
        if lista[i] < menor_elemento:
            menor_elemento = lista[i]
            indice_menor = i

    if indice_menor == 0:
        return 0

    lista[0], lista[indice_menor] = lista[indice_menor], lista[0]

    return 1