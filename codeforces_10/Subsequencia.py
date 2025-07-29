Sa,Sb = map(int, input().split())

elementos_1 = list(map(int, input().split()))
elementos_2= list(map(int, input().split()))
esta_na_outra_lista = []

i= 0
j= 0

while i < Sa and j < Sb:
    if elementos_1[i] == elementos_2[j]:
        j+=1

    i+=1

if j == Sb:
    print("S")
else:
    print("N")