def contar_posicoes(mensagem_cifrada, crib):
    tamanho_mensagem = len(mensagem_cifrada)
    tamanho_crib = len(crib)
    posicoes_validas = 0

    for i in range (tamanho_mensagem - tamanho_crib +1):
        posicao_valida = True

        for j in range(tamanho_crib):
            if crib[j] == mensagem_cifrada [i +j]:
                posicao_valida = False
                break
        if posicao_valida:
            posicoes_valida+=1

    return posicoes_validas

mensagem_cifrada = input()
crib = input()

print(contar_posicoes(mensagem_cifrada, crib))
