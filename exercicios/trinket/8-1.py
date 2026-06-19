def verificaPrimaridade(n : int):
  divisores = []
  
  for i in range(1, n + 1):
    if n%i==0:
      divisores.append(i)
  
  if len(divisores)> 2:
    print(f"{n} não é primo, os divisores são : {divisores}")
  else:
    print(f"{n} é primo")



n = int(input("Qual o valor de N? "))
print("Digite os valores:")
valores= []
primos = []
for i in range(n):
  v=int(input())
  valores.append(v)

for v in valores:
  verificaPrimaridade(v)