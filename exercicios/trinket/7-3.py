quantidade = int(input("Quantos nomes? "))
nomes = []
for i in range(quantidade):
  nome = input()
  nomes.append(nome)

inversa = nomes.reverse()

for nome in nomes:
  print(nome)