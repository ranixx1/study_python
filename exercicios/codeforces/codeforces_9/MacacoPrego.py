teste_num = 1
while True:
    N = int(input())
    if N == 0:
        break

    x_intersecao = -10001
    y_intersecao = 10001
    u_intersecao = 10001
    v_intersecao = -10001

    primeiro_retangulo = True

    for _ in range(N):
        x, y, u, v = map(int, input().split())

        if primeiro_retangulo:
            x_intersecao = x
            y_intersecao = y
            u_intersecao = u
            v_intersecao = v
            primeiro_retangulo = False
        else:
            x_intersecao = max(x_intersecao, x)
            y_intersecao = min(y_intersecao, y)
            u_intersecao = min(u_intersecao, u)
            v_intersecao = max(v_intersecao, v)

    print(f"Teste {teste_num}")

    if x_intersecao > u_intersecao or v_intersecao > y_intersecao:
        print("nenhum")
    else:
        print(f"{x_intersecao} {y_intersecao} {u_intersecao} {v_intersecao}")
    
    print()
    teste_num += 1