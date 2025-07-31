N = int(input())
estoque = [0] * (N + 1)

for i in range(1, N + 1):
    estoque[i] = int(input())

P = int(input())
vendas_efetuadas = 0

for _ in range(P):
    tamanho_pedido = int(input())
    
    if 1 <= tamanho_pedido <= N and estoque[tamanho_pedido] > 0:
        vendas_efetuadas += 1
        estoque[tamanho_pedido] -= 1
        
print(vendas_efetuadas)