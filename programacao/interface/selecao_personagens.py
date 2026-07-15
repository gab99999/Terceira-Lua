import pygame
import random

# Controle de FPS
clock = pygame.time.Clock()

# Tamanho da tela
WIDTH, HEIGHT = 1280, 720

# Cores
CINZA = (100, 100, 100, 180)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

# Configuração da animação
num_personagens = 6
frame = 0
ultimo_tempo = 0


personagem_escolhido = None

def main():
    global frame, ultimo_tempo

    # Inicializa o pygame
    pygame.init()

    # Cria a janela do jogo
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Lista dos frames dos ícones
    frame_icons = []

    

    # Carrega e redimensiona os frames dos personagens
    for i in range(6):
        frame_icon = pygame.image.load(
            r"programacao\interface\assets\frame_selecao.png"
        ).convert_alpha()

        frame_icon = pygame.transform.scale(
            frame_icon,
            (
                int(frame_icon.get_width() * 0.5),
                int(frame_icon.get_height() * 0.5)
            )
        )

        frame_icons.append(frame_icon)

    # Cria os retângulos dos frames
    frame_icons_rect = []

    for icon in frame_icons:
        frame_icons_rect.append(icon.get_rect())


    def desenhar_texto(surface, texto, fonte, cor, x, y, largura_max):
        palavras = texto.split()
        linha = ""

        for palavra in palavras:
            teste = linha + palavra + " "

            if fonte.size(teste)[0] <= largura_max:
                linha = teste
            else:
                render = fonte.render(linha, True, cor)
                surface.blit(render, (x, y))
                y += fonte.get_height() + 5
                linha = palavra + " "

        if linha:
            render = fonte.render(linha, True, cor)
            surface.blit(render, (x, y))
        

    # Carrega as oito rotações de um personagem
    def carregar_rotacoes(pasta):
        direcoes = [
            "north",
            "north-east",
            "east",
            "south-east",
            "south",
            "south-west",
            "west",
            "north-west",
        ]

        return [
            pygame.image.load(fr"{pasta}\{d}.png").convert_alpha()
            for d in direcoes
        ]

    nomes_personagens = [
    "Amara",
    "Antonius",
    "Nicholas",
    "Perfidia",
    "Raoni",
    "Taina"
]
    
    descricoes = []

    # Carrega todos os personagens
    frame_personagens = [
        carregar_rotacoes(
            fr"programacao\interface\assets\personagens\{nome}\rotations"
        )
        for nome in nomes_personagens
    ]

    
    # Carrega as descrições dos personagens
    for nome in nomes_personagens:
        with open(
            fr"programacao\interface\assets\personagens\{nome}\descricao.md",
            "r",
            encoding="utf-8"
        ) as arquivo:
            descricoes.append(arquivo.read())

    
    # Cria os retângulos dos personagens
    frame_personagens_rect = []

    for personagem in frame_personagens:
        frame_personagens_rect.append(personagem[0].get_rect())

    # Cria o painel de seleção
    frame_selecao_rect = pygame.Rect(0, 0, 400, 720)
    frame_selecao_surface = pygame.Surface(frame_selecao_rect.size, pygame.SRCALPHA)
    frame_selecao_surface.fill(CINZA)

    # Cria o painel de descrição
    frame_descricao_rect = pygame.Rect(880, 0, 400, 720)
    frame_descricao_surface = pygame.Surface(frame_descricao_rect.size, pygame.SRCALPHA)
    frame_descricao_surface.fill(CINZA)

    # Carrega o plano de fundo
    background = pygame.image.load(
        r"programacao\interface\assets\fundos\background_selecao_personagens.png"
    ).convert()



    # Define as posições dos personagens
    posicoes = [
        (70, 140),
        (190, 140),
        (70, 280),
        (190, 280),
        (70, 420),
        (190, 420),
    ]

    # Posiciona os personagens
    for rect, pos in zip(frame_personagens_rect, posicoes):
        rect.topleft = pos

    # Posiciona os frames dos personagens
    for rect, (x, y) in zip(frame_icons_rect, posicoes):
        rect.topleft = (x + 4, y + 4)


    fonte_nome = pygame.font.SysFont("Arial", 48)
    # Nomes dos presonagens

    fonte_descricao = pygame.font.SysFont("Arial", 24)


    # Controla o loop principal
    running = True
    while running:

        # Obtém a posição do mouse
        mouse_pos = pygame.mouse.get_pos()

        mouse_click = pygame.mouse.get_pressed()[0]

        # Processa os eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i in range(6):
                    if frame_icons_rect[i].collidepoint(event.pos):
                        personagem_escolhido = nomes_personagens[i]
                        running = False

        # Desenha o plano de fundo
        screen.blit(background, (0, 0))

        # Desenha os painéis
        screen.blit(frame_selecao_surface, frame_selecao_rect.topleft)
        screen.blit(frame_descricao_surface, frame_descricao_rect.topleft)

        # Atualiza o frame da animação
        agora = pygame.time.get_ticks()

        if agora - ultimo_tempo > 120:
            frame = (frame + 1) % 8
            ultimo_tempo = agora

        # Exemplo da animação do primeiro personagem
        screen.blit(frame_personagens[0][frame], frame_personagens_rect[0])

        # Desenha os frames dos personagens
        for i in range(6):
            screen.blit(frame_icons[i], frame_icons_rect[i])

        # Desenha todos os personagens voltados para o sul
        for personagem, rect in zip(frame_personagens, frame_personagens_rect):
            screen.blit(personagem[4], rect)

        # Exibe uma versão ampliada do personagem ao passar o mouse
        for i in range(6):
            if frame_icons_rect[i].collidepoint(mouse_pos):
                personagem = frame_personagens[i][frame]

                personagem = pygame.transform.scale(
                    personagem,
                    (
                        int(personagem.get_width() * 4),
                        int(personagem.get_height() * 4)
                    )
                )

                rect = personagem.get_rect(
                    center=((WIDTH // 2), HEIGHT // 2 + 50)
                )

                texto_nome_personagem = fonte_nome.render(
                    nomes_personagens[i],
                    True,
                    BRANCO
                )

                screen.blit(texto_nome_personagem, (1010, 40))

                desenhar_texto(
                    screen,
                    descricoes[i],
                    fonte_descricao,
                    BRANCO,
                    900,
                    120,
                    350
                )

                screen.blit(personagem, rect)

        # Atualiza a tela
        pygame.display.flip()

        # Limita o jogo a 60 FPS
        clock.tick(60)

    return personagem_escolhido

if __name__ == "__main__":
    main()

#auxilio da i.a para a criação de um GIF e textos comportarem corretamente em suas devidas caixas