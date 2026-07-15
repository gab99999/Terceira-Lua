import pygame
import random
from pathlib import Path
from batalha import GerenciadorBatalha, EstadoBatalha

BASE_DIR = Path(__file__).parent    

def main(personagem):

    pygame.init()

    WIDTH = 1280
    HEIGHT = 720

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Batalha")

    clock = pygame.time.Clock()

    fonte = pygame.font.SysFont("Arial", 28)
    fonte_titulo = pygame.font.SysFont("Arial", 42)
    fonte_log = pygame.font.SysFont("Arial", 20)

    background = pygame.image.load(
        BASE_DIR / "assets" / "fundos" / "background_batalha.png"
    ).convert()

    background_lua = pygame.image.load(
        BASE_DIR / "assets" / "fundos" / "background_batalha_terceira_lua.png"
    ).convert()

    BRANCO = (255,255,255)
    PRETO = (25,25,25)
    VERDE = (0,200,0)
    VERMELHO = (200,0,0)
    AMARELO = (255,220,0)
    AZUL = (70,120,255)

    def desenhar_barra(x,y,vida,max_vida):

        largura = 250
        altura = 20

        pygame.draw.rect(screen, VERMELHO, (x,y,largura,altura))

        vida_atual = largura * (vida/max_vida)

        pygame.draw.rect(screen, VERDE, (x,y,vida_atual,altura))

    transicao_lua = False
    alpha_lua = 0
    lua_animacao = False

    nomes_personagens = [
        "Amara",
        "Antonius",
        "Nicholas",
        "Perfidia",
        "Raoni",
        "Taina"
    ]

    inimigo = random.choice(
        [nome for nome in nomes_personagens if nome != personagem]
    )

    batalha = GerenciadorBatalha(personagem, inimigo)
    estado = batalha.iniciar_combate()

    jogador = estado["jogador"]
    bot = estado["bot"]

    imagem_personagem = pygame.image.load(
        BASE_DIR / "assets" / "personagens" / personagem / "rotations" / "east.png"
    ).convert_alpha()

    imagem_inimigo = pygame.image.load(
            BASE_DIR / "assets" / "personagens" / inimigo / "rotations" / "west.png"
    ).convert_alpha()

    imagem_inimigo = pygame.transform.scale(imagem_inimigo,
(
    imagem_inimigo.get_width()*3,
    imagem_inimigo.get_height()*3
)
    )

    imagem_personagem = pygame.transform.scale(
        imagem_personagem,
        (
            imagem_personagem.get_width()*3,
            imagem_personagem.get_height()*3
        )
    )
    
    habilidades = {
    "Amara": [
        "Reação Mágica",
        "Ondas Elevadas",
        "Cura Envenenada"
    ],

    "Antonius": [
        "Soco Tático",
        "Granada de Luz",
        "Tiro Certeiro"
    ],

    "Nicholas": [
        "Absorver Calor",
        "Aquecer Matéria",
        "Fusão Mágica"
    ],

    "Perfidia": [
        "Invocação Lunar",
        "Pluralidade Estelar",
        "Brutalizar as Luas"
    ],

    "Raoni": [
        "Foco em Penas",
        "Especialização em Aves",
        "Inversão Curativa"
    ],

    "Taina": [
        "Dilaceração Dupla",
        "Arremesso de Lâmina",
        "Apunhalada Pacífica"
    ]
}
    
    opcoes = habilidades[personagem] + ["Interações"]

    selecionado = 0

    mensagem = "..."

    rodando = True

    while rodando:

        estado = batalha.resumo()

        historico = estado["historico"][-5:]

        jogador = estado["jogador"]
        bot = estado["bot"]

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if estado["estado"] == EstadoBatalha.FIM_BATALHA:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

            if estado["estado"] == EstadoBatalha.TURNO_JOGADOR:

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:
                        selecionado = (selecionado-1)%4

                    elif event.key == pygame.K_DOWN:
                        selecionado = (selecionado+1)%4

                    elif event.key == pygame.K_RETURN:

                        if selecionado == 0:
                            estado = batalha.executar_acao("habilidade_1")

                        elif selecionado == 1:
                            estado = batalha.executar_acao("habilidade_2")

                        elif selecionado == 2:
                            estado = batalha.executar_acao("habilidade_3")

                        else:
                            interacoes = estado["interacoes_disponiveis"]

                            if interacoes:
                                estado = batalha.executar_acao(
                                    "interacao",
                                    interacoes[0]
                                )


        if estado["terceira_lua_ativa"] and not lua_animacao:
            lua_animacao = True
            transicao_lua = True
            alpha_lua = 0

        

        if transicao_lua:

            screen.blit(background, (0, -150))

            fundo = background_lua.copy()
            fundo.set_alpha(alpha_lua)
            screen.blit(fundo, (0, -150))

            alpha_lua += 6

            if alpha_lua >= 255:
                alpha_lua = 255
                transicao_lua = False

        elif estado["terceira_lua_ativa"]:
            screen.blit(background_lua, (0, -150))

        else:
            screen.blit(background, (0, -150))

        titulo = fonte.render("LOG DA BATALHA", True, AMARELO)
        screen.blit(titulo, (360, 550))        

        screen.blit(fonte_titulo.render(personagem,True,BRANCO),(175,180))
        screen.blit(fonte_titulo.render(inimigo,True,BRANCO),(970,180))

        desenhar_barra(
                    100,
                    130,
                    jogador["vida"],
                    jogador["vida_maxima"]
                )
        desenhar_barra(
                    900,
                    130,
                    bot["vida"],
                    bot["vida_maxima"]
                )
        



        screen.blit(
    fonte.render(
        f'HP {jogador["vida"]}/{jogador["vida_maxima"]}',
        True,
        BRANCO
    ),
    (165,155)
)
        screen.blit(
    fonte.render(
        f'HP {bot["vida"]}/{bot["vida_maxima"]}',
        True,
        BRANCO
    ),
    (960,155)
)

        screen.blit(imagem_personagem, (50,150))
        screen.blit(imagem_inimigo, (840,150))

        pygame.draw.line(screen, BRANCO, (330, 540), (330, 720), 2)
        pygame.draw.rect(screen,PRETO,(0,540,1280,180))

        y = 580

        for linha in historico:
            texto = fonte_log.render(linha, True, BRANCO)
            screen.blit(texto, (865, y))
            y += 24

        if estado["estado"] == EstadoBatalha.FIM_BATALHA:
            texto = fonte_titulo.render(
                "Pressione ENTER para voltar",
                True,
                AMARELO
            )
            screen.blit(texto, (470, 400))

        for i,opcao in enumerate(opcoes):

            cor = BRANCO

            if i == selecionado and estado["estado"] == EstadoBatalha.TURNO_JOGADOR:
                cor = AMARELO

            texto = fonte.render(opcao,True,cor)

            screen.blit(texto,(50,570+i*30))

        pygame.display.flip()

        clock.tick(60)