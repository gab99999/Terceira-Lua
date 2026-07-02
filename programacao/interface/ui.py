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

# FPS
clock = pygame.time.Clock()



# Imagens
logo = pygame.image.load(r"")

background = pygame.image.load(r"programacao\interface\assets\background.png").convert()

painel = pygame.image.load(r"programacao\interface\assets\ai-made\menu_frame.png").convert_alpha()

painel = pygame.transform.scale(
    painel,
    (painel.get_width() * 2.5, painel.get_height() * 2.5)
)

painel_rect = painel.get_rect(center=(WIDTH / 2, (HEIGHT / 2) + 100))

botao_jogar = pygame.image.load(r"programacao\interface\assets\ai-made\jogar_button.png").convert_alpha()

botao_jogar = pygame.transform.scale(
    botao_jogar,
    (botao_jogar.get_width() * 2.4, botao_jogar.get_height() * 2.4)
)

botao_jogar_rect = botao_jogar.get_rect(center=(painel_rect.centerx, painel_rect.centery - 74))

botao_sair = pygame.image.load(r"programacao\interface\assets\ai-made\sair_button.png").convert_alpha()

botao_sair = pygame.transform.scale(
    botao_sair,
    (botao_sair.get_width() * 2.4, botao_sair.get_height() * 2.4)
)

botao_sair_rect = botao_sair.get_rect(center=(painel_rect.centerx, painel_rect.centery - 8))

# Fonte
fonte = pygame.font.SysFont(None, 40)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Clique do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 

            # Botão sair
             if botao_sair_rect.collidepoint(event.pos):
                running = False

            # Ir para tela de seleção de personagens
             if botao_jogar_rect.collidepoint(event.pos):
                import selecao_personagens
                selecao_personagens.main()
                running = False

    # Desenha o fundo
    screen.blit(background, (0, 0))

    # Desenha o painel
    screen.blit(painel, painel_rect)

    # Desenha o botão jogar
    screen.blit(botao_jogar, botao_jogar_rect)

    # Desenha o botão sair
    screen.blit(botao_sair, botao_sair_rect)

    # Atualiza a tela
    pygame.display.flip()

    # FPS
    clock.tick(60)

pygame.quit()