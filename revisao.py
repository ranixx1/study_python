a = list(map(int, input().split()))
lista_ordenada = sorted(a)
for i in range(len(lista_ordenada)-1):
    if lista_ordenada[i+1]-lista_ordenada[i] == lista_ordenada[i+2] - lista_ordenada[i+1]:
        print("PA")
    else:
        print("NÃo é")