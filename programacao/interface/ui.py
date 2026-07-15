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

# Controle de FPS
clock = pygame.time.Clock()

# Imagens
background = pygame.image.load(r"programacao\interface\assets\fundos\background.png").convert()

logo = pygame.image.load(r"programacao\interface\terceira lua png.png").convert_alpha()

# Redimensiona a logo
logo = pygame.transform.scale(
    logo,
    (logo.get_width() * 0.6, logo.get_height() * 0.6)
)

# Posição da logo
logo_rect = logo.get_rect(center=(WIDTH / 2, (HEIGHT / 2) - 150))

#imagem painel
painel = pygame.image.load(r"programacao\interface\assets\ai-made\menu_frame.png").convert_alpha()

# Redimensiona o painel
painel = pygame.transform.scale(
    painel,
    (painel.get_width() * 2.5, painel.get_height() * 2.5)
)

# Posição do painel
painel_rect = painel.get_rect(center=(WIDTH / 2, (HEIGHT / 2) + 150))

# Imagem botão jogar
botao_jogar = pygame.image.load(r"programacao\interface\assets\ai-made\jogar_button.png").convert_alpha()

# Redimensiona o botão Jogar
botao_jogar = pygame.transform.scale(
    botao_jogar,
    (botao_jogar.get_width() * 2.4, botao_jogar.get_height() * 2.4)
)

# Posição do botão Jogar
botao_jogar_rect = botao_jogar.get_rect(center=(painel_rect.centerx, painel_rect.centery - 74))

# Imagem botão sair
botao_sair = pygame.image.load(r"programacao\interface\assets\ai-made\sair_button.png").convert_alpha()

# Redimensiona o botão Sair
botao_sair = pygame.transform.scale(
    botao_sair,
    (botao_sair.get_width() * 2.4, botao_sair.get_height() * 2.4)
)

# Posição do botão Sair
botao_sair_rect = botao_sair.get_rect(center=(painel_rect.centerx, painel_rect.centery - 8))

# Fonte
fonte = pygame.font.SysFont(None, 40)

# Controla o loop principal
running = True
while running:

    # Processa os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Clique do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                # Botão Sair
                if botao_sair_rect.collidepoint(event.pos):
                    running = False

                # Vai para a tela de seleção de personagens
                if botao_jogar_rect.collidepoint(event.pos):
                    import selecao_personagens
                    import tela_batalha

                    personagem = selecao_personagens.main()

                    if personagem is not None:
                        tela_batalha.main(personagem)

                    running = False

    # Desenha o fundo
    screen.blit(background, (0, 0))

    # Desenha a logo
    screen.blit(logo, logo_rect)

    # Desenha o painel
    screen.blit(painel, painel_rect)

    # Desenha o botão Jogar
    screen.blit(botao_jogar, botao_jogar_rect)

    # Desenha o botão Sair
    screen.blit(botao_sair, botao_sair_rect)

    # Atualiza a tela
    pygame.display.flip()

    # Limita o jogo a 60 FPS
    clock.tick(60)

pygame.quit()

# Uso de i.a para grande parte do aprendizado de PYGAME e criação de imagens