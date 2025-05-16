a, b, c = map(int, input().split())

# Verificar se forma um triângulo
if a + b <= c or a + c <= b or b + c <= a:
    print("n")
else:
    # Descobrir qual é o maior lado
    if a >= b and a >= c:
        maior = a
        menor1 = b
        menor2 = c
    elif b >= a and b >= c:
        maior = b
        menor1 = a
        menor2 = c
    else:
        maior = c
        menor1 = a
        menor2 = b

    soma_quadrados = menor1**2 + menor2**2
    maior_quadrado = maior**2

    if soma_quadrados > maior_quadrado:
        print("a")  # acutângulo
    elif soma_quadrados == maior_quadrado:
        print("r")  # retângulo
    else:
        print("o")  # obtusângulo
