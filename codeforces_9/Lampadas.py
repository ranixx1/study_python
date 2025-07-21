N = int(input())
numeros = list(map(int, input().split()))

lampada_A = 0
lampada_B = 0

for numero in numeros:
    if numero == 1:
        lampada_A = 1 - lampada_A
    elif numero == 2:
        lampada_A = 1 - lampada_A
        lampada_B = 1 - lampada_B

print(lampada_A)
print(lampada_B)