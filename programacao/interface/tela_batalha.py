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
    fonte_dano = pygame.font.SysFont("Arial", 60, bold=True)

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

    


    tomou_dano = False
    tempo_dano = 0

    animacao_ataque = False
    tempo_ataque = 0
    atacante = None

    esperando_ataque = False
    tempo_espera = 0

    dano_visual = None
    dano_y = 250
    dano_alpha = 255

    dano_inimigo_visual = None
    dano_inimigo_y = 250
    dano_inimigo_alpha = 255

    tempo_dano_inimigo = 0

    # animação do inimigo atacando
    animacao_ataque_inimigo = False
    tempo_ataque_inimigo = 0

    # dano recebido pelo jogador
    dano_jogador_visual = None
    dano_jogador_y = 250
    dano_jogador_alpha = 255
    tempo_dano_jogador = 0

    esperando_ataque_inimigo = False
    tempo_espera_inimigo = 0

    rodando = True

    while rodando:

        estado = batalha.resumo()

        historico = estado["historico"][-5:]

        jogador = estado["jogador"]
        bot = estado["bot"]

        if esperando_ataque:

            if pygame.time.get_ticks() - tempo_espera > 1000:
                esperando_ataque = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if estado["estado"] == EstadoBatalha.FIM_BATALHA:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return


            
            if estado["estado"] == EstadoBatalha.TURNO_JOGADOR and not esperando_ataque:

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:
                        selecionado = (selecionado-1)%4

                    elif event.key == pygame.K_DOWN:
                        selecionado = (selecionado+1)%4

                    elif event.key == pygame.K_RETURN:

                        vida_jogador_antes = jogador["vida"]
                        vida_inimigo_antes = bot["vida"]

                        if selecionado == 0:
                            estado = batalha.executar_acao("habilidade_1")
                            esperando_ataque = True
                            tempo_espera = pygame.time.get_ticks()

                        elif selecionado == 1:
                            estado = batalha.executar_acao("habilidade_2")
                            esperando_ataque = True
                            tempo_espera = pygame.time.get_ticks()                            

                        elif selecionado == 2:
                            estado = batalha.executar_acao("habilidade_3")
                            esperando_ataque = True
                            tempo_espera = pygame.time.get_ticks()


                        dano = vida_inimigo_antes - estado["bot"]["vida"]
                        dano_recebido = vida_jogador_antes - estado["jogador"]["vida"]

                        if dano > 0:

                            dano_visual = int(dano)

                            dano_y = 250
                            dano_alpha = 255

                            tomou_dano = True
                            tempo_dano = pygame.time.get_ticks()

                            animacao_ataque = True
                            tempo_ataque = pygame.time.get_ticks()
                            atacante = "jogador"

                        if dano_recebido > 0:

                            esperando_ataque_inimigo = True
                            tempo_espera_inimigo = pygame.time.get_ticks()

                        else:
                            pass


        if esperando_ataque_inimigo:

            tempo = pygame.time.get_ticks() - tempo_espera_inimigo

            if tempo > 1000:  # 1 segundo esperando

                dano_jogador_visual = int(dano_recebido)

                dano_jogador_y = 250
                dano_jogador_alpha = 255

                tempo_dano_jogador = pygame.time.get_ticks()

                animacao_ataque_inimigo = True
                tempo_ataque_inimigo = pygame.time.get_ticks()

                esperando_ataque_inimigo = False

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


        
        if dano_visual:

            tempo = pygame.time.get_ticks() - tempo_ataque

            # sobe
            dano_y -= 2

            # desaparece aos poucos
            dano_alpha = max(0, 255 - int(tempo * 0.35))

            texto_dano = fonte_dano.render(
                f"-{dano_visual}",
                True,
                VERMELHO
            )

            texto_dano.set_alpha(dano_alpha)

            screen.blit(
                texto_dano,
                (850, dano_y)
            )

            if tempo > 800:
                dano_visual = None
                dano_alpha = 255

        if dano_jogador_visual:

            tempo = pygame.time.get_ticks() - tempo_dano_jogador

            dano_jogador_y -= 2

            dano_jogador_alpha = max(
                0,
                255 - int(tempo * 0.35)
            )

            texto = fonte_dano.render(
                f"-{dano_jogador_visual}",
                True,
                VERMELHO
            )

            texto.set_alpha(dano_jogador_alpha)

            screen.blit(
                texto,
                (250, dano_jogador_y)
            )

            if tempo > 800:
                dano_jogador_visual = None


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
        
        
        pos_jogador = 50
        pos_inimigo = 840

        if animacao_ataque and atacante == "jogador":

            tempo = pygame.time.get_ticks() - tempo_ataque

            if tempo < 150:
                pos_jogador = 120

            if tempo < 100:
                pos_inimigo = 780

            elif tempo < 200:
                pos_inimigo = 840


        if animacao_ataque_inimigo:

            tempo = pygame.time.get_ticks() - tempo_ataque_inimigo

            if tempo < 100:
                pos_jogador = 35

            elif tempo < 200:
                pos_jogador = 65

            else:
                animacao_ataque_inimigo = False

        if tomou_dano:

            tempo = pygame.time.get_ticks() - tempo_dano

            if tempo < 100:
                pos_inimigo = 825

            elif tempo < 200:
                pos_inimigo = 855

            elif tempo < 300:
                pos_inimigo = 840

            else:
                tomou_dano = False
            

        if dano_inimigo_visual:

            tempo = pygame.time.get_ticks() - tempo_dano_inimigo

            dano_inimigo_y -= 2

            dano_inimigo_alpha = max(
                0,
                255 - int(tempo * 0.35)
            )

            texto = fonte_dano.render(
                f"-{dano_inimigo_visual}",
                True,
                VERMELHO
            )

            texto.set_alpha(dano_inimigo_alpha)

            screen.blit(
                texto,
                (100, dano_inimigo_y)
            )

            if tempo > 800:
                dano_inimigo_visual = None

        screen.blit(imagem_inimigo, (pos_inimigo,150))

        screen.blit(imagem_personagem, (pos_jogador,150))

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