C = int(input())

saldo_atual = 100
maior_premiacao = 100

for _ in range(C):
    valor_caixa = int(input())
    saldo_atual += valor_caixa

    if saldo_atual > maior_premiacao:
        maior_premiacao = saldo_atual

print(maior_premiacao)