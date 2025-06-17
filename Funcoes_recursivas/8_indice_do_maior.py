def indice_do_maior(lista, i=0, maior_i=0):
    if i == len(lista):
        return maior_i
    if lista[i] > lista[maior_i]:
        maior_i = i
    return indice_do_maior(lista, i + 1, maior_i)
