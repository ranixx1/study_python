N = int(input())

numeros = list(map(int, input().split()))
soma = sum(numeros)


media = soma / N

abaixo_media = 0
acima_ou_igual_media = 0

for num in numeros:
    if num < media:
        abaixo_media += 1
    else:
        acima_ou_igual_media += 1

print(f"{media:.1f}")
print(abaixo_media)
print(acima_ou_igual_media)