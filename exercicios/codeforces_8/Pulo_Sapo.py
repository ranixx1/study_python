p, n = map(int, input().split())
alturas_canos = list(map(int, input().split()))
pode_vencer = True
for i in range(n - 1):
    diferenca_altura = abs(alturas_canos[i+1] - alturas_canos[i])

    if diferenca_altura > p:
        pode_vencer = False
        break 

if pode_vencer:
    print("YOU WIN")
else:
    print("GAME OVER")