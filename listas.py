Qtd_letras = int(input())
palavra = input()
qtd_repete=0
for i in range(len(palavra) - 1): 
    if palavra[i] == palavra[i+1]:
        qtd_repete += 1 

print(qtd_repete)
        
