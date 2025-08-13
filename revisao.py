lista = list(map(int, input().split()))
alternada = True
for i in range(len(lista)-1):
    if lista[i] % 2 == lista[i+1]%2:
        alternada = False
        break

if alternada:
    print("alternada")
else:
    print("Não alternada")