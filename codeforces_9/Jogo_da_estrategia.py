#A entrada consiste de duas linhas. A primeira linha contém dois inteiros J e R, o número de jogadores e de rodadas respectivamente (1 ≤ J, R ≤ 500). A segunda linha contém J × R inteiros, correspondentes aos Pontos de Vitória em cada uma das jogadas feitas, na ordem em que aconteceram. Os Pontos de Vitória obtidos em cada jogada serão sempre inteiros entre 0 e 100, inclusive.

def encontrar_vencedor_jogo():
    J, R = map(int, input().split())
    pontos_vitoria = list(map(int, input().split()))
    pontuacoes_jogadores = [0] * J
    for i in range(len(pontos_vitoria)):
        jogador_atual_indice = i % J
        pontuacoes_jogadores[jogador_atual_indice] += pontos_vitoria[i]
    max_pontuacao = -1
    vencedor = -1
    for i in range(J):
        if pontuacoes_jogadores[i] >= max_pontuacao:
            max_pontuacao = pontuacoes_jogadores[i]
            vencedor = i
    print(vencedor + 1)
encontrar_vencedor_jogo()