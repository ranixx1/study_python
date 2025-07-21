N = int(input())
numeros = list(map(int, input().split()))

if N <= 2:
    print(1)
else:
    escadinhas = 1
    
    diff_anterior = numeros[1] - numeros[0] 
    
    for i in range(2, N):
        diff_atual = numeros[i] - numeros[i-1]
        
        if diff_atual != diff_anterior:
            escadinhas += 1
            diff_anterior = diff_atual
            
    print(escadinhas)