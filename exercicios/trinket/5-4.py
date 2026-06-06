x1, y1, x2, y2, x, y = map(int, input().split())

if x1 <= x <= x2 and y1 <= y <= y2:
    print("Dentro!")
else:
    print("Fora!")