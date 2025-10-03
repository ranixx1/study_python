l,d = input().split()
l = int(l)
d = int(d)
k,p = input().split()
k = int(k)
p = int(p)
custo_km = k*l
custo_pedagio = (l // d) * p
custo_total = custo_km + custo_pedagio
custo_total = int(custo_total)
print(custo_total)
#l = o comprimento da estrada 
#d = a distância entre pedágios
#k = custo por quilômetro percorrido 
#p = valor de cada pedágio