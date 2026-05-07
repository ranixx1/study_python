print("Informe as pontuações dos atletas. Digite -1 para encerrar")
numeros_lista = []
numeros = int(input())
while(numeros != -1):
    numeros = int(input())
    numeros_lista.append(numeros)

print(f"O recorde de pontos é {max(numeros_lista)}.")

