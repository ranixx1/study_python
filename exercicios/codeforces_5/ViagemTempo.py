a, b, c = map(int, input().split())

permutacoes = [
    (a, b, c),
    (a, c, b),
    (b, a, c),
    (b, c, a),
    (c, a, b),
    (c, b, a)
]
resposta = "N"
for perm in permutacoes:
    if perm[0] - perm[1] == 0 or perm[0] - perm[1] + perm[2] == 0:
        resposta = "S"
        break
    if perm[0] + perm[1] == 0 or perm[0] + perm[1] - perm[2] == 0:
        resposta = "S"
        break

print(resposta)
