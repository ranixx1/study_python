valor_i = int(input())
qtd_compra = int(input())
valor_pagar = int(input())
total = valor_i*qtd_compra
troco = valor_pagar - total

print(f"A pagar: {total}")
print(f"Troco  : {troco}")
