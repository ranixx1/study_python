#Você deve escrever um programa que, dados o preço do litro de álcool, o preço do litro de gasolina e os quilômetros por litro que um carro bi-combustível realiza com cada um desses combustíveis
pre_al, pre_gs, km_l_al, km_l_gs = map(float, input().split())

#determine se é mais econômico abastecer os carros da CTT com álcool ou com gasolina. No caso de não haver diferença de custo entre abastecer com álcool ou gasolina a CTT prefere utilizar gasolina.

consumo_total_al = km_l_al /pre_al
consumo_total_gs = km_l_gs /pre_gs

if consumo_total_gs > consumo_total_al:
    print("G")

elif consumo_total_gs == consumo_total_al:
    print("G")
else:
    print("A")