meses = ["null","janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]

mes_escolhido = int(input("Qual o número do mês? "))
if mes_escolhido == 0 or mes_escolhido >12:
    print(f"Erro: não existe mês de número {mes_escolhido}! Por favor, digite um número entre 1 e 12.")
else:
    print(f"O mês é {meses[mes_escolhido]}")