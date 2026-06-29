import pygame

pygame.init()

# Cores
BRANCO = (255, 255, 255) 
PRETO = (0, 0, 0) 
VERMELHO = (255, 0, 0) 
AZUL = (0, 0, 255) 
VERDE = (0, 255, 0)

# Tela
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

clock = pygame.time.Clock()

# Imagens
background = pygame.image.load(r"programacao\interface\assets\background.png").convert()

botao = pygame.image.load(r"programacao\interface\assets\ai-made\jogar_button.png").convert_alpha()

painel = pygame.image.load(r"programacao\interface\assets\ai-made\menu_frame.png").convert_alpha()

# Fonte
fonte = pygame.font.SysFont(None, 40)

# Posição do botão
botao_rect = botao.get_rect(topleft=(100, 500))
painel_rect = painel.get_rect(topleft=(100, 500))

running = True

while running:

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Desenha o fundo
    screen.blit(background, (0, 0))

    # Desenha o botão
    screen.blit(botao, botao_rect)

    screen.blit(painel, painel_rect)


    # Atualiza a tela
    pygame.display.flip()

    # FPS
    clock.tick(60)

pygame.quit()