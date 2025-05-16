C = int(input())
A = int(input())

# Cada viagem leva no máximo C - 1 alunos (1 monitor obrigatório)
max_alunos_por_viagem = C - 1

# Número mínimo de viagens necessárias
viagens = (A + max_alunos_por_viagem - 1) // max_alunos_por_viagem

print(viagens)
