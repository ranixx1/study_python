nPessoas = int(input("Qual o número de pessoas? "))
age = map(int, input().split())

media = int(sum(age)/nPessoas)

print(f"A média de idade das pessoas é {media} anos")