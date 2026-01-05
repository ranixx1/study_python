import pygame
import sys
import random

# ---------------- INIT ----------------
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("Nenhum controle detectado")
    sys.exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

# ---------------- TELA ----------------
LARGURA, ALTURA = 800, 450
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Quadrado Runner - PS2")

clock = pygame.time.Clock()
fonte = pygame.font.SysFont("arial", 24)

# ---------------- PLAYER ----------------
player = pygame.Rect(100, 320, 40, 40)
vel_y = 0
no_chao = True

# ---------------- OBSTÁCULOS ----------------
obstaculos = []
spawn_timer = 0

pontuacao = 0
gravidade = 1
vel_pulo = -15
vel_jogo = 6

mapa_botoes = {
    2: "X",
    1: "O"
}

# ---------------- LOOP ----------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Botão X = pulo
        if event.type == pygame.JOYBUTTONDOWN:
            if mapa_botoes.get(event.button) == "X" and no_chao:
                vel_y = vel_pulo
                no_chao = False

            # Botão O = sair
            if mapa_botoes.get(event.button) == "O":
                pygame.quit()
                sys.exit()

    # ---------------- CONTROLE ANALÓGICO ----------------
    eixo_x = joystick.get_axis(0)
    player.x += int(eixo_x * 6)

    # Limite da tela
    if player.x < 0:
        player.x = 0
    if player.x > LARGURA - player.width:
        player.x = LARGURA - player.width

    # ---------------- FÍSICA ----------------
    vel_y += gravidade
    player.y += vel_y

    if player.y >= 320:
        player.y = 320
        vel_y = 0
        no_chao = True

    # ---------------- OBSTÁCULOS ----------------
    spawn_timer += 1
    if spawn_timer > 90:
        spawn_timer = 0
        obstaculos.append(pygame.Rect(800, 340, 30, 30))

    for obs in obstaculos:
        obs.x -= vel_jogo

    obstaculos = [o for o in obstaculos if o.x > -50]

    # ---------------- COLISÃO ----------------
    for obs in obstaculos:
        if player.colliderect(obs):
            pygame.quit()
            sys.exit()

    # ---------------- PONTUAÇÃO ----------------
    pontuacao += 0.5

    # ---------------- DESENHO ----------------
    tela.fill((25, 25, 25))

    # Chão
    pygame.draw.rect(tela, (100, 100, 100), (0, 360, 800, 5))

    # Player
    pygame.draw.rect(tela, (0, 200, 255), player)

    # Obstáculos
    for obs in obstaculos:
        pygame.draw.rect(tela, (255, 80, 80), obs)

    # HUD
    texto = fonte.render(f"Pontos: {pontuacao}", True, (255, 255, 255))
    tela.blit(texto, (10, 10))

    info = fonte.render("X = Pular | O = Sair", True, (180, 180, 180))
    tela.blit(info, (10, 40))

    pygame.display.flip()
    clock.tick(60)
