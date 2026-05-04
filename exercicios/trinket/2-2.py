valorCompra = int(input("Qual o valor da compra? "))
metodoPay = input("Como gostaria de pagar à vista(V) ou à prazo (P)? ")

if(metodoPay == "V"):
    valorCompra = valorCompra - (valorCompra*0.05)
    valorCompra = int(valorCompra)
    print(f"Valor à pagar: {valorCompra}")


if(metodoPay == "P"):
    valorCompra = valorCompra + (valorCompra*0.08)
    valorCompra = int(valorCompra)
    print(f"Valor à pagar: {valorCompra}")
    parcela = int(valorCompra/3)
    print(f"Parcela 1: {parcela}")
    print(f"Parcela 2: {parcela}")
    print(f"Parcela 3: {parcela}")

