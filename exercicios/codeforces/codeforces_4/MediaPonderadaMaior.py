nota1,nota2 = map(int, input().split())
nota3,nota4 = map(int, input().split())
p1,p2 =map(int, input().split())

total_1=(nota1*p1+nota2*p2)/p1+p2
total_2=(nota3*p1+nota4*p2)/p1+p2
if total_1 > total_2:
    print("1")
elif total_2 > total_1:
    print("2")
elif total_1 == total_2:
    print("1")
