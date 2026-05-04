peso = int(input("Peso: "))
altura = float(input("Altura: "))

imc = peso/(altura*altura)

if(imc < 18.5):
    print("Abaixo do peso")
elif(imc > 18.5 and imc < 25):
    print("Peso normal")
elif(imc >=25 and imc < 30):
    print("Sobrepeso")
elif(imc > 30):
    print("Obesidade")
