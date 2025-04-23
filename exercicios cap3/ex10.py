item_venda = int(input("Digite o valor do item: "))
quantidade = int(input("Digite a quantidade de itens:"))
valor_pago = int(input("Digite quanto você vai pagar:"))
total= item_venda*quantidade
troco= valor_pago - total
print(f"total a pagar: {total}")
print(f"troco: {troco}")
