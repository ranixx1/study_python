 
R, G, B = map(int, input().split())
 
valores = sorted([R, G, B])
 
 
if (valores[1] - valores[0]) == (valores[2] - valores[1]):
    print('S')
else:
    print('N')