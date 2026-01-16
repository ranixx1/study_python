# [PRODUTO || CATEGORIA || VALOR || STATUS] => BASE DE DADOS

pedidos = [
    ("Camisa", "Vestuário", 59.90, "Entregue"),
    ("Tênis", "Calçados", 199.90, "Cancelado"),
    ("Calça", "Vestuário", 89.90, "Entregue"),
    ("Fone de Ouvido", "Eletrônicos", 129.90, "Pendente"),
    ("Meia", "Vestuário", 19.90, "Entregue"),
    ("Notebook", "Eletrônicos", 3259.90, "Entregue"),
    ("Jaqueta", "Vestuário", 139.90, "Cancelado"),
]

# Funções de chamada
def filter_by_category(categoria):
    for i in pedidos:
        if categoria == i[1]:
            print(f"pedido: {i[0]}_____ Valor(R$): {i[2]}")
    return f"--------Busca completa---------"          
             
def filter_by_disponibility(money_real):
    for i in pedidos:
        if money_real >= i[2]:
            print(f"pedido: {i[0]}_____ Valor(R$): {i[2]}")
    print("Nenhum produto disponível")
    return f"--------Busca completa---------"          

def filter_by_status(status):
    for i in pedidos:
        if status == i[3]:
            print(f"pedido:{i[0]}____ Valor(R$):{i[2]}")
    return f"--------Busca completa---------"          

def return_totalsum():
    soma = 0
    for i in pedidos:
        soma = soma + i[2]
    return f"Soma total de produtos: {soma:.2f}"

def return_qtd():
    return f"Quantidade total de pedidos: {len(pedidos)}"


print(filter_by_disponibility(9))