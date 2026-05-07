def fatorial(n):
    if(n == 0):
        return 1
    else:
        return n * fatorial(n-1)

n = int(input("Digite um número: "))
if(n == 0):
    print("O número deve ser maior que 0.")
else:
    print(fatorial(n))