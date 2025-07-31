N = int(input())
fita = list(map(int, input().split()))

resultado = [float('inf')] * N

distancia_do_zero = float('inf')
for i in range(N):
    if fita[i] == 0:
        distancia_do_zero = 0
    else:
        distancia_do_zero += 1
    resultado[i] = distancia_do_zero

distancia_do_zero = float('inf')
for i in range(N - 1, -1, -1):
    if fita[i] == 0:
        distancia_do_zero = 0
    else:
        distancia_do_zero += 1
    resultado[i] = min(resultado[i], distancia_do_zero)

for i in range(N):
    if resultado[i] >= 9:
        resultado[i] = 9

print(' '.join(map(str, resultado)))