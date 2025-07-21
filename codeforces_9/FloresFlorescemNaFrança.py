while True:
    sentenca = input()
    if sentenca == '*':
        break
 
    palavras = sentenca.split()
    
    primeira_letra_base = palavras[0][0].lower()
    
    e_tautograma = True
    for i in range(1, len(palavras)):
        if palavras[i][0].lower() != primeira_letra_base:
            e_tautograma = False
            break
            
    if e_tautograma:
        print('Y')
    else:
        print('N')
        