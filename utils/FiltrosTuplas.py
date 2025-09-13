pedidos = [
    ("Camisa", "Vestuário", 59.90, "Entregue"),
    ("Tênis", "Calçados", 199.90, "Cancelado"),
    ("Calça", "Vestuário", 89.90, "Entregue"),
    ("Fone de Ouvido", "Eletrônicos", 129.90, "Pendente"),
    ("Meia", "Vestuário", 19.90, "Entregue"),
    ("Notebook", "Eletrônicos", 3259.90, "Entregue"),
    ("Jaqueta", "Vestuário", 139.90, "Cancelado"),
]

# FILTROS

filtro = input("Digite a categoria que deseja: ")

# FILTRO POR CATEGORIA
for i in pedidos:
    if filtro == i[1]:
        print(f"pedido: {i[0]}_____ Valor: (R$): {i[2]}")

#FILTRO POR VALOR
quantia = float(input("Digite o valor que possui: "))
for i in pedidos:
    if quantia >= i[2]:
        print(f"opções disponiveis: {i[0]}_____Valor: (R$): {i[2]}")


