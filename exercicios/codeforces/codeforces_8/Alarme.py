# programa que, dada a hora corrente e a hora do alarme, determine o número de minutos que ela poderia dormir.

while True:
    h1, m1, h2, m2 = map(int, input().split())
    
    # Verifica o sinalizador de fim de entrada
    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break 
    
    Hora_minuto_h1 = h1 * 60 + m1
    Hora_minuto_toque = h2 * 60 + m2
    
    minutos_diferenca = Hora_minuto_toque - Hora_minuto_h1
    
    # Se a hora do alarme for menor que a hora atual, significa que o alarme é no dia seguinte
    if minutos_diferenca < 0:
        minutos_diferenca += 24 * 60 # Adiciona os minutos de um dia completo
        
    print(minutos_diferenca)