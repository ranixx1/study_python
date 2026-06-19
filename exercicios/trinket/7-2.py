n = int(input("Quantidade de jogadores? "))

saques = []
bloqueios = []
ataques = []

saques_sucesso = []
bloqueios_sucesso = []
ataques_sucesso = []

print("Digite os dados para cada jogador:")

for i in range(n):
    dados = input().split()

    nome = dados[0]
    s = int(dados[1])
    b = int(dados[2])
    a = int(dados[3])
    s1 = int(dados[4])
    b1 = int(dados[5])
    a1 = int(dados[6])

    saques.append(s)
    bloqueios.append(b)
    ataques.append(a)

    saques_sucesso.append(s1)
    bloqueios_sucesso.append(b1)
    ataques_sucesso.append(a1)

perc_saque = (sum(saques_sucesso) / sum(saques)) * 100
perc_bloqueio = (sum(bloqueios_sucesso) / sum(bloqueios)) * 100
perc_ataque = (sum(ataques_sucesso) / sum(ataques)) * 100

print("As estatísticas do jogo são as seguintes:")
print(f"Pontos de Saque: {perc_saque:.2f} %")
print(f"Pontos de Bloqueio: {perc_bloqueio:.2f} %")
print(f"Pontos de Ataque: {perc_ataque:.2f} %")