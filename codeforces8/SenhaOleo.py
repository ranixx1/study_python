caso = 1

while True:
    try:
        n = int(input()) 
        oleosidades = list(map(float, input().split())) 

        lista_teclas = [] 
        for i in range(10):
            lista_teclas.append([i, oleosidades[i]])

        for i in range(10):
            for j in range(i + 1, 10):
                if (lista_teclas[i][1] < lista_teclas[j][1]) or (
                    lista_teclas[i][1] == lista_teclas[j][1] and lista_teclas[i][0] > lista_teclas[j][0]
                ):
                    lista_teclas[i], lista_teclas[j] = lista_teclas[j], lista_teclas[i]

        senha = ''
        for i in range(n):
            senha += str(lista_teclas[i][0])

        print(f"Caso {caso}: {senha}")
        caso += 1

    except EOFError:
        break
