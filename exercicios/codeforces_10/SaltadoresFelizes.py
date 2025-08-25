while True:
    try:
        entrada = input().split()
        if not entrada:
            continue
 
        n = int(entrada[0])
        numeros = [int(x) for x in entrada[1:]]
 
        if n == 1:
            print('Alegre')
            continue
 
        diferencas = []
        for i in range(n - 1):
            diferenca_abs = abs(numeros[i] - numeros[i+1])
            diferencas.append(diferenca_abs)
        
        diferencas.sort()
        
        esperado = list(range(1, n))
 
        if diferencas == esperado:
            print('Alegre')
        else:
            print('Nao alegre')
 
    except EOFError:
        break
    except (ValueError, IndexError):
        continue