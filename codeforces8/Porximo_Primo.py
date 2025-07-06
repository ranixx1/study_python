def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, num+1):
        if num % i == 0:
            return False
    return True

def proximo_primo (num_inicial):
    proximo_candidato = num_inicial + 1
    while(True):
        if eh_primo(proximo_candidato):
            return proximo_candidato
        proximo_candidato+=1
n = int(input("Digite um número: "))

proximo = proximo_primo(n)

print(proximo)
