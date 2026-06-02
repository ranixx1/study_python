valores = []
while(True):
  n = int(input())
  if(n == 0): break
  valores.append(n)

print(f"O seu maior gasto hoje foi R$ {max(valores):.2f}")