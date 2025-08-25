N = int(input())

numeros = list(map(int,input().split()))
soma = sum(numeros)

media = soma / N

abaixo_media_lista = []
acima_ou_igual_media_lista = []

for num in numeros:
    if num< media:
        abaixo_media_lista.append(num)
    else:
        acima_ou_igual_media_lista.append(num)

print(f"{media:.1f}")
print(f"{len(abaixo_media_lista)} {' '.join(map(str, abaixo_media_lista))}")
print(f"{len(acima_ou_igual_media_lista)} {' '.join(map(str, acima_ou_igual_media_lista))}")