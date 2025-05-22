nc1, dc1, vc1 = map(int, input().split())
nc2, dc2, vc2 = map(int, input().split())

# Converter velocidade de km/h para m/s
vc1 = vc1 * (5 / 18)
vc2 = vc2 * (5 / 18)

# Calcular o tempo para cada charrete
t1 = dc1 / vc1
t2 = dc2 / vc2

# Verificar quem chega primeiro
if t1 < t2:
    print(nc1)
else:
    print(nc2)
