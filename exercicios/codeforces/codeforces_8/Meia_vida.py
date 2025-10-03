#Um determinado material radioativo perde metade de sua massa a cada s segundos. Escreva um programa que leia o tempo s de perda de massa e a massa inicial mi, em gramas, de um material. O programa deve então calcular em quanto tempo a massa do material fica menor do que 0, 5 grama. O programa deve mostrar a massa final, com 3 casas decimais em uma linha e o tempo gasto para o material chegar a essa massa. O tempo deve ser mostrado na forma D dias HH:MM:SS.


s, mi = map(int,input().split())

massa_atual = float(mi)
tempo_total_seg = 0
while massa_atual >= 0.5:
    massa_atual= massa_atual/2
    tempo_total_seg = tempo_total_seg + s

dias = tempo_total_seg// (24 * 3600)
tempo_restante_segundos = tempo_total_seg % (24 * 3600)
horas = tempo_restante_segundos // 3600
tempo_restante_segundos %= 3600
minutos = tempo_restante_segundos // 60
segundos = tempo_restante_segundos % 60

print(f"{dias} dias {horas:02d}:{minutos:02d}:{segundos:02d}")



