def soma_algarismos(n):
    if n == 0:
        return n
    else:
        return (n%10+soma_algarismos(n//10))
    
n = int(input())
print(soma_algarismos(n))

