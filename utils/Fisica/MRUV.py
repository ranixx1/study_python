# Função 1: V = V0 + at
def calculaVelocidade_por_tempo(VelocidadeInicial, aceleracao, tempo):
    """Calcula a velocidade final usando o tempo (V = V0 + at)."""
    return f"Velocidade = {VelocidadeInicial + aceleracao * tempo}"

# Função 2: V² = V0² + 2aΔS (Equação de Torricelli)
def calculaVelocidade_por_espaco(VelocidadeInicial, aceleracao, deltaEspaco):
    """Calcula o QUADRADO da velocidade final usando o espaço (V² = V0² + 2aΔS)."""
    # Nota: Esta função retorna V², não V.
    return f"V² = {VelocidadeInicial**2 + 2 * aceleracao * deltaEspaco}"

# Função 3: S = S0 + V0t + (at²)/2 (Sorvetão)
def calculaEspaco(espacoInicial, VelocidadeInicial, tempo, aceleracao):
    """Calcula a posição final (S = S0 + V0t + at²/2)."""
    return f"Espaço = {espacoInicial + VelocidadeInicial * tempo + aceleracao * (tempo**2) / 2}"

# Função 4: ΔS = (V + V0)/2 * t
def calculaDeltaEspaco(velocidade, velocidadeInicial, deltaTempo):
    """Calcula o deslocamento usando a velocidade média."""
    return f"Delta Espaço = {((velocidade + velocidadeInicial) / 2) * deltaTempo}"
