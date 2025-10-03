#1 se o carro B precisa acelerar; −1 se precisa desacelerar; ou 0 se precisa manter a velocidade atual.
A = int(input())
B = int(input())
C = int(input())

"""
O carro B precisa ser acelerado se a distância da sua traseira para a traseira do carro A for menor do que a distância da sua traseira para a traseira do carro C. Se for maior, ele precisa ser desacelerado. Se for igual, precisa manter a velocidade atual. Quer dizer, o carro B precisa ser acelerado se (B-A) < (C-B), desacelerado se (B-A) > (C-B) e manter a velocidade se (B-A) for igual a (C-B).""" 
if (B-A)< (C-B):
    print(1)
elif (B-A)> (C-B):
    print(-1)
else:
    print(0)