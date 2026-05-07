pessoas = ["Daniel", "Aluizio","Isabel", "Teles", "Eduardo"]

verifica = input("Qual nome você quer verificar? ")
for pessoa in pessoas:
    if verifica == pessoa:
        print(f"O nome {verifica} está na lista, acesso permitido!")
        break
    else:
         print(f"O nome {verifica} não está na lista, acesso negado!")