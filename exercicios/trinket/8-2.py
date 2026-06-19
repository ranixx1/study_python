def retornaSomaDosNPares(arr):
    soma = 0
    for i in arr:   
        if(i%2 == 0):
            soma+=i
    print(f"Soma dos números pares: {soma}")


lista =[]
for i in range(4):
  n = int(input(f"Digite número {i+1}: "))
  lista.append(n)

retornaSomaDosNPares(lista)