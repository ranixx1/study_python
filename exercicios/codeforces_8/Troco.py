def calcular_troco(dinheiro: int, valor_produto: float) -> float:
    quant_p = dinheiro // valor_produto
    gastos = valor_produto * quant_p
    return dinheiro - gastos


def troco_maximo(dinheiro: int, quant_marcas: int) -> str:
    l_produtos = list(map(float, input().split()))
    m_troco = -1
    for i in range(quant_marcas):
        if l_produtos[i] <= dinheiro:
            troco = calcular_troco(dinheiro, l_produtos[i])
            if troco > m_troco:
                m_troco = troco
    if m_troco >= 0:
        return "{:.2f}".format(m_troco)
    else:
        return "0.00"


casos = int(input())
for i in range(casos):
    dinheiro, q_marcas = map(int, input().split())
    print(troco_maximo(dinheiro, q_marcas))