N, R = map(int, input().split())

retornaram = set(map(int, input().split()))

todos_voluntarios = set(range(1, N + 1))


nao_retornaram = sorted(list(todos_voluntarios - retornaram))

if not nao_retornaram:
    print("*")
else:
    print(*nao_retornaram, "")