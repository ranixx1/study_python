def criaTrianguloNumerico(n : int):
    if(n <0):
        print("Valor invalido!")
    else:
        for i in range(1, n + 1):
            for j in range(i):
                print(i, end=" ")
            print()
        
n = int(input("Digite o valor de n: "))
criaTrianguloNumerico(n)