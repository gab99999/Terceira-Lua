import pygame
from pathlib import Path
from dados_personagens import habilidades

BASE_DIR = Path(__file__).parent

clock = pygame.time.Clock()

largura, altura = 1280, 720

CINZA = (100, 100, 100, 180)
BRANCO = (255, 255, 255)

num_personagens = 6
frame = 0
ultimo_tempo = 0


personagem_escolhido = None

def main():
    global frame, ultimo_tempo

    pygame.init()

    screen = pygame.display.set_mode((largura, altura))

    frame_icons = []
    
    for i in range(6):
        frame_icon = pygame.image.load(
            BASE_DIR / "assets" / "frame_selecao.png"
        ).convert_alpha()

        frame_icon = pygame.transform.scale(
            frame_icon,
            (
                int(frame_icon.get_width() * 0.5),
                int(frame_icon.get_height() * 0.5)
            )
        )

        frame_icons.append(frame_icon)

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
            pygame.image.load(pasta / f"{d}.png").convert_alpha()
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

    frame_personagens = [
    carregar_rotacoes(
        BASE_DIR / "assets" / "personagens" / nome / "rotations"
    )
    for nome in nomes_personagens
]

    for nome in nomes_personagens:
        with open(
            BASE_DIR / "assets" / "personagens" / nome / "descricao.md", encoding="utf-8"
        ) as arquivo:
            descricoes.append(arquivo.read())

    
    frame_personagens_rect = []

    for personagem in frame_personagens:
        frame_personagens_rect.append(personagem[0].get_rect())

    frame_selecao_rect = pygame.Rect(0, 0, 400, 720)
    frame_selecao_surface = pygame.Surface(frame_selecao_rect.size, pygame.SRCALPHA)
    frame_selecao_surface.fill(CINZA)

    frame_descricao_rect = pygame.Rect(880, 0, 400, 720)
    frame_descricao_surface = pygame.Surface(frame_descricao_rect.size, pygame.SRCALPHA)
    frame_descricao_surface.fill(CINZA)

    background = pygame.image.load(
        BASE_DIR / "assets" / "fundos" / "background_selecao_personagens.png"
    ).convert()

    posicoes = [
        (70, 140),
        (190, 140),
        (70, 280),
        (190, 280),
        (70, 420),
        (190, 420),
    ]

    for rect, pos in zip(frame_personagens_rect, posicoes):
        rect.topleft = pos

    for rect, (x, y) in zip(frame_icons_rect, posicoes):
        rect.topleft = (x + 4, y + 4)


    fonte_nome = pygame.font.SysFont("Arial", 48)
    fonte_habilidade = pygame.font.SysFont("Arial", 32)

    fonte_descricao = pygame.font.SysFont("Arial", 24)

    running = True
    while running:

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i in range(6):
                    if frame_icons_rect[i].collidepoint(event.pos):
                        personagem_escolhido = nomes_personagens[i]
                        running = False

        screen.blit(background, (0, 0))

        screen.blit(frame_selecao_surface, frame_selecao_rect.topleft)
        screen.blit(frame_descricao_surface, frame_descricao_rect.topleft)

        agora = pygame.time.get_ticks()

        if agora - ultimo_tempo > 120:
            frame = (frame + 1) % 8
            ultimo_tempo = agora

        screen.blit(frame_personagens[0][frame], frame_personagens_rect[0])

        for i in range(6):
            screen.blit(frame_icons[i], frame_icons_rect[i])

        for personagem, rect in zip(frame_personagens, frame_personagens_rect):
            screen.blit(personagem[4], rect)

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
                    center=((largura // 2), altura // 2 + 50)
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


                nome = nomes_personagens[i]

                texto_habilidades = fonte_habilidade.render(
                    "Habilidades:",
                    True,
                    BRANCO
                )

                screen.blit(texto_habilidades, (900, 400))


                y = 450

                for habilidade in habilidades[nome]:
                    texto = fonte_descricao.render(
                        habilidade,
                        True,
                        BRANCO
                    )

                    screen.blit(texto, (900, y))
                    y += 30

        
        pygame.display.flip()

        clock.tick(60)

    return personagem_escolhido

if __name__ == "__main__":
    main()
