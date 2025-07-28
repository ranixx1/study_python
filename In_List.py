Sa,Sb = map(int, input().split())

elementos_1 = list(map(int, input().split()))
elementos_2= list(map(int, input().split()))
esta_na_outra_lista = []

for elemento in elementos_1:
    if elemento in elementos_2:
        esta_na_outra_lista.append(elemento)
    else:
        elemento= elemento+1

print(esta_na_outra_lista)