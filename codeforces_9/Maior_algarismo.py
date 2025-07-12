def soma_algarismos(numero):
    soma = 0
    for digito_str in str(numero):
        soma += int(digito_str)
    return soma

while True:
    N1, N2 = map(int, input().split())

    if N1 == 0 and N2 == 0:
        break

    soma1 = soma_algarismos(N1)
    soma2 = soma_algarismos(N2)

    if soma1 > soma2:
        print(soma1)
    else:
        print(soma2)