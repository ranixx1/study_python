# Leitura dos níveis dos jogadores
A = int(input())
B = int(input())
C = int(input())
D = int(input())

diff1 = abs((A + B) - (C + D))
diff2 = abs((A + C) - (B + D))
diff3 = abs((A + D) - (B + C))


if diff1 <= diff2 and diff1 <= diff3:
    menor_dif = diff1
elif diff2 <= diff1 and diff2 <= diff3:
    menor_dif = diff2
else:
    menor_dif = diff3


print(menor_dif)
