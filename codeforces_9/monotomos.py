Qtd_letras = int(input())
palavra = input()
tamanho_palavra = len(palavra)

qtd_repete = 0

for i in range(tamanho_palavra-1):
    if palavra[i] == palavra[i+1]:
        qtd_repete+=1
        

print(qtd_repete)

