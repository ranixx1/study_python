def soma_algarismos(numero):
    soma = 0
    for digito_str in str(numero):
        soma += int(digito_str)
    if soma >= 10:
        return soma_algarismos(str(soma))
    else:
        return soma

while True:
    N1, N2 = map(int, input().split())

    if N1 == 0 and N2 == 0:
        break

    soma1 = soma_algarismos(N1)
    soma2 = soma_algarismos(N2)

    if soma1 > soma2:
        print("1")
    elif soma2 > soma1:
        print("2")
    else:
        print("0")
    