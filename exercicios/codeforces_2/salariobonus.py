nome = input()
salario = float(input())
vendas = float(input())
comissao = 0.15 * vendas
novo_salario = salario + comissao
print(nome)
print(f"R$ {novo_salario:.2f}")