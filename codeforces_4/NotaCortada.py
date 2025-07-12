B = int(input())
b = int(input())

# Área do pedaço da esquerda (Felix)
area_felix = (B + b) * 70 / 2

# Área total da nota
area_total = 160 * 70
metade = area_total / 2

if area_felix > metade:
    print(1)  
elif area_felix < metade:
    print(2)  
else:
    print(0) 
