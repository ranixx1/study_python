#6º
a,b =(input().split())
numa= int(a)
numb= int(b)
p1, p2 = (input().split())
peso1 = int(p1)
peso2 = int(p2)
somap = peso1+peso2
somap = int(somap)
mediapond = (numa*peso1 + numb*peso2)/somap
mediapond = int(mediapond)
print(mediapond)