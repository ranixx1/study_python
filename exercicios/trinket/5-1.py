valor_compra = int(input("Qual o valor da compra?"))
tipo_pagamento = input("Como gostaria de pagar: à vista (V) ou à prazo (P)? ")

if(tipo_pagamento == "V" or tipo_pagamento == "v"):
   valor_compra = valor_compra -(valor_compra*0.08)
   print(f"Valor à pagar: {valor_compra}")
elif(tipo_pagamento == "P" or tipo_pagamento == "p"):
  valor_compra = valor_compra + (valor_compra*0.08)
  parcela = valor_compra/3
  for i in range(3):
    print(f"Parcela {i+1}: {parcela}")