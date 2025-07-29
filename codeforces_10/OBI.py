Participantes,pontos_minimo = map(int,input().split())
passou=0
for i in range(0, Participantes):
    fase_1, fase_2 = map(int,input().split())
    if fase_1 + fase_2 >= pontos_minimo:
        passou+=1
        i+=1
    else:
        i+=1
print(passou)