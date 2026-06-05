quantidade_casos = int(input())

for _ in range(quantidade_casos):
    x, y = map(int, input().split())

    if x % 2 == 0:
        x += 1

    soma = 0

    while y > 0:
        soma += x
        x += 2
        y -= 1

    print(soma)