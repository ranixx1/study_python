

a,b,c,d = map(int,input().split())

if a<0 or b<0 or c<0 or d<0:

    maior = -999999999

    if a<0 and a>maior:
        maior = a
    if b<0 and b>maior:
        maior = b
    if c<0 and c>maior:
        maior = c
    if d<0 and d>maior:
        maior = d
    print(maior)
        
        
        