N = int(input())
pilhas = list(map(int, input().split()))

soma_total_pedras = sum(pilhas)

soma_escada_base = N * (N - 1) // 2

if soma_total_pedras < soma_escada_base:
    print(-1)
else:
    if (soma_total_pedras - soma_escada_base) % N != 0:
        print(-1)
    else:
        h = (soma_total_pedras - soma_escada_base) // N
        escada_perfeita = [h + i for i in range(N)]
        
        movimentos = 0
        for i in range(N):
            if pilhas[i] > escada_perfeita[i]:
                movimentos += pilhas[i] - escada_perfeita[i]
        
        print(movimentos)