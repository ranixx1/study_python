n = int(input())  # Número de jogos
ganhos = 0
 
for _ in range(n):
    porta_do_carro = int(input())
    if porta_do_carro != 1:
        ganhos += 1
 
print(ganhos)