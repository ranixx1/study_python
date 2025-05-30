X, Y = map(int, input().split())  # Tamanho da página
L1, H1 = map(int, input().split())  # Foto 1
L2, H2 = map(int, input().split())  # Foto 2
 
# Lista com as duas orientações possíveis
orientacoes_foto1 = [(L1, H1), (H1, L1)]
orientacoes_foto2 = [(L2, H2), (H2, L2)]
 
# Flag false
encaixa = False
 
# Testa todas as combinações de orientações
for l1, h1 in orientacoes_foto1:
    for l2, h2 in orientacoes_foto2:
        # lado na horizontal
        if (l1 + l2 <= X and max(h1, h2) <= Y) or (l1 + l2 <= Y and max(h1, h2) <= X):
            encaixa = True
        # vertical
        if (max(l1, l2) <= X and h1 + h2 <= Y) or (max(l1, l2) <= Y and h1 + h2 <= X):
            encaixa = True
print('S' if encaixa else 'N')