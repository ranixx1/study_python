def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

n = int(input())
numeros= map(int,input().split())
for x in numeros:    
    divisores = 0
    
    for divisor in range(1, x + 1):
        if (x % divisor == 0):
            divisores += 1
        
    if (divisores == 2):
        print(f"{x}! = {fatorial(x)}")