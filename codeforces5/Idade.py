idadeMonica= int(input())
idadefilho1=int(input())
idadefilho2=int(input())
idadefilho3= idadeMonica - idadefilho1 - idadefilho2

if idadefilho1 > idadefilho2 and idadefilho1>idadefilho3:
    print(idadefilho1)
elif idadefilho2> idadefilho1 and idadefilho2>idadefilho3:
    print(idadefilho2)
elif idadefilho3> idadefilho1 and idadefilho3>idadefilho2:
    print(idadefilho3)