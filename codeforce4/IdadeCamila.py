idade_1 = int(input())
idade_2 = int(input())
idade_3 = int(input())

if idade_1 >= idade_2 >= idade_3 or idade_3 >= idade_2 >= idade_1:
    print(idade_2)
elif idade_2 >= idade_1 >= idade_3 or idade_3 >= idade_1 >= idade_2:
    print(idade_1)
elif idade_1 >= idade_3 >= idade_2 or idade_2 >= idade_3 >= idade_1:
    print(idade_3)