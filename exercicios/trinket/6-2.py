while True:
    n = int(input())

    if n == 0:
        break

    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(f"{abs(i - j) + 1:3d}")
        print(" ".join(linha))

    print()