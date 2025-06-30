

n = int(input())
qtd_divisores =0
for i in range (1, n+1):
    if n%i==0:
        qtd_divisores +=1
   
if qtd_divisores == 2:
    print("Sim")
else:
    print("Nao")
