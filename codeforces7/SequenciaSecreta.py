n = int(input())
sequencia = [int(input()) for _ in range(n)]
 
contador = 0
ultimo = 0
 
for num in sequencia:
    if num != ultimo:
        contador += 1
        ultimo = num
 
print(contador)