n = int(input("Qual o N? "))

lista = []

print("Digite os valores:")
for i in range(n):
    lista.append(int(input()))

op = int(input("Qual a op? "))
a = int(input("Qual o A? "))
b = int(input("Qual o B? "))

valor_a = lista[a - 1]
valor_b = lista[b - 1]

if op == 0:
    print(f"{valor_a} + {valor_b} = {valor_a + valor_b}")
elif op == 1:
    print(f"{valor_a} * {valor_b} = {valor_a * valor_b}")
else:
    print("Operação inválida.")