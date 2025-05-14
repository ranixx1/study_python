#Dados o consumo do carro, a distância em que se encontra do aeroporto e a quantidade de combustível presente no tanque antes do abastecimento, determine qual deve ser a menor quantidade de combustível que Cássio deve comprar

consumo_l = int(input())
distancia_a = int(input())
qtd_no_tanque = int(input())

total = distancia_a / consumo_l- qtd_no_tanque
if qtd_no_tanque * consumo_l >= distancia_a:
    print("0.0")
else:
    print(f"{total:.1f}")