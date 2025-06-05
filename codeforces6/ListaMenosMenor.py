#Escreva uma função que receba uma lista e retorne uma nova lista com todos os elementos da lista recebida, sem o menor.

def sublista_sem_menor(lista):
    menor_elemento = min(lista)
    nova_lista = []
    menor_removido = False
    for elemento in lista:
        if elemento == menor_elemento and not menor_removido:
            menor_removido = True 
        else:
            nova_lista.append(elemento) #
    return nova_lista
