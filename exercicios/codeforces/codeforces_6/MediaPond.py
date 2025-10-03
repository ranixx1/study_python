#Escreva uma função que receba dois números inteiros, dois pesos, e retorne a média ponderada dos mesmos.
def media_ponderada(v1, p1, v2, p2):
    media = ((v1*p1 ) + (v2*p2)) / (p1+p2)
    return media