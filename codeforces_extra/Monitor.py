proporcao = input().strip()
L_ratio, H_ratio = map(int, proporcao.split(':'))
D_polegadas = float(input())
D_cm = D_polegadas * 2.54
 
 
k = D_cm / (L_ratio**2 + H_ratio**2)**0.5
 
L = k * L_ratio
H = k * H_ratio
 
 
print("{0:.2f}".format(L))
print("{0:.2f}".format(H))