consumo = int(input())

# Valor fixo da assinatura
valor = 7

if consumo <= 10:
    valor = 7

elif consumo <= 30:
    valor += (consumo - 10) * 1

elif consumo <= 100:
    valor += (20)  
    valor += (consumo - 30) * 2

else: 
    valor += (20)  
    valor += (70 * 2) 
    valor += (consumo - 100) * 5  

print(valor)
