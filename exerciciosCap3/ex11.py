s = int(input("Digite a distância entre as cidades em km: "))
v = int(input("Digite a velocidade do carro em km/h: "))
t = s / v  # Tempo em horas

horas = int(t)
minutos = int((t - horas) * 60)

print(f"{horas}:{minutos}")