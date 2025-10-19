x = int(input())
divisores = 0
for i in range(1,x+1):
    if(x%i ==0):
        divisores +=1
if(divisores ==2):
    print("primo")
else:
    print("não primo")
