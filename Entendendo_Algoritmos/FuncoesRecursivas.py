def procure_pela_chave(caixa):
        for item in caixa:
            if item.e_uma_caixa:
                procure_pela_chave(item)
            elif item.e_uma_chave():
                print("achei a chave")

def regressiva(i):
    print(i)
    if i <=1: #  CASO BASE
        return
    else:        # CASO RECURSIVO
        regressiva(i-1)

