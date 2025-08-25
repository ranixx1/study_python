numero_de_competidores = int(input())
qtd_aprovados_minimo = int(input())
lista_notas = []

for _ in range(numero_de_competidores):
    nota = int(input())
    lista_notas.append(nota)

lista_notas.sort(reverse=True)

if qtd_aprovados_minimo == 0:
    print(0)
else:
    nota_corte = lista_notas[qtd_aprovados_minimo - 1]
    
    classificados_finais = qtd_aprovados_minimo
    
    for i in range(qtd_aprovados_minimo, numero_de_competidores):
        if lista_notas[i] == nota_corte:
            classificados_finais += 1
        else:
            break
            
    print(classificados_finais)