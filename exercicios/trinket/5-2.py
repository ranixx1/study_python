n1 = float(input("Qual é a nota da primeira unidade? "))
n2 = float(input("Qual é a nota da segunda unidade?"))
n3 = float(input("Qual é a nota da terceira unidade?"))

media = (n1*2+n2*3+n3*4)/9

if(media >= 7):
    print("Francisco está aprovado")
elif(media >3):
    print("Francisco está em prova final")
else:
     print("Francisco está reprovado")