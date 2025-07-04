senha= 9842
senha_solicitada= 0
while senha_solicitada != senha:
    print("Senha Invalida!")
    senha_solicitada= int(input())
    if senha_solicitada == senha:
        print("Acesso Permitido.")
        break