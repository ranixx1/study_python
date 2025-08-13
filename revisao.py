def soma_impares(lista):
    if len(lista)== 0:
        return []
        
    else:
        r = soma_impares(lista[:-1])
        if lista[-1]%2!=0:
            r.append(lista[-1])
        return r

lista = list(map(int,input().split()))
lista.append(12)
print(sum(soma_impares(lista)))