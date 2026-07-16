import pygame
from pathlib import Path

BASE_DIR = Path(__file__).parent


def main():

    pygame.init()

    pygame.mixer.music.load(
        BASE_DIR.parent / "soundtrack" / "Batalha_das_Luas.mp3"
    )
    pygame.mixer.music.play(-1)

    # Tela
    WIDTH, HEIGHT = 1280, 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Menu")

    clock = pygame.time.Clock()

    background = pygame.image.load(
        BASE_DIR / "assets" / "fundos" / "background.png"
    ).convert()

    logo = pygame.image.load(
        BASE_DIR / "terceira lua png.png"
    ).convert_alpha()

    logo = pygame.transform.scale(
    logo,
    (
        int(logo.get_width() * 0.6),
        int(logo.get_height() * 0.6)
    )
)

    # Posição da logo
    logo_rect = logo.get_rect(center=(WIDTH / 2, (HEIGHT / 2) - 150))

    #imagem painel
    painel = pygame.image.load(
        BASE_DIR / "assets" / "ai-made" / "menu_frame.png"
    )

    # Redimensiona o painel
    painel = pygame.transform.scale(
        painel,
        (painel.get_width() * 2.5, painel.get_height() * 2.5)
    )

    # Posição do painel
    painel_rect = painel.get_rect(center=(WIDTH / 2, (HEIGHT / 2) + 150))

    # Imagem botão jogar
    botao_jogar = pygame.image.load(
        BASE_DIR / "assets" / "ai-made" / "jogar_button.png"
    ).convert_alpha()

    # Redimensiona o botão Jogar
    botao_jogar = pygame.transform.scale(
        botao_jogar,
        (botao_jogar.get_width() * 2.4, botao_jogar.get_height() * 2.4)
    )

    # Posição do botão Jogar
    botao_jogar_rect = botao_jogar.get_rect(center=(painel_rect.centerx, painel_rect.centery - 74))

    # Imagem botão sair
    botao_sair = pygame.image.load(
        BASE_DIR / "assets" / "ai-made" / "sair_button.png"
    ).convert_alpha()

    # Redimensiona o botão Sair
    botao_sair = pygame.transform.scale(
        botao_sair,
        (botao_sair.get_width() * 2.4, botao_sair.get_height() * 2.4)
    )

    # Posição do botão Sair
    botao_sair_rect = botao_sair.get_rect(center=(painel_rect.centerx, painel_rect.centery - 8))

    fonte_creditos = pygame.font.SysFont(None, 22)

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
                        from interface import selecao_personagens
                        from interface import tela_batalha

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

        creditos = [
            "Trilha Sonora: Batalha das Luas",
            "Composição: Yasmin Pereira Lucas",
            "Todos os direitos reservados."
        ]

        y = HEIGHT - 70

        for linha in creditos:
            texto = fonte_creditos.render(linha, True, (255, 255, 255))
            screen.blit(texto, (20, y))
            y += 18

        # Atualiza a tela
        pygame.display.flip()

        # Limita o jogo a 60 FPS
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

    # Uso de i.a para grande parte do aprendizado de PYGAME e criação de imagens