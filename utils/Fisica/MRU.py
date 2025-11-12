
def calculaDistancia(velocidade,tempo):
    return f"Distância = {velocidade*tempo}"

def calculaTempo(distancia,velocidade):
    return f"Tempo = {distancia/velocidade}"

def calculaVelocidade(distancia,tempo):
    return f"Velocidade = {distancia/tempo}"

def calculaEspaço(EspaçoInicial,velocidade,tempo):
    return f"Espaço = {EspaçoInicial+velocidade*tempo}"

def calculaVelocidadeMedia(deltaEspaco,deltaTempo):
    return f"Velocidade média = {deltaEspaco/deltaTempo}"