import pygame
import random


pygame.init()


# =========================
# CONFIGURAÇÕES
# =========================

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Batalha")

clock = pygame.time.Clock()


# =========================
# FONTES
# =========================

fonte = pygame.font.SysFont("Arial", 28)
fonte_titulo = pygame.font.SysFont("Arial", 42)


# =========================
# CORES
# =========================

BRANCO = (255,255,255)
PRETO = (25,25,25)

VERDE = (0,200,0)
VERMELHO = (200,0,0)

AMARELO = (255,220,0)


# =========================
# BACKGROUND
# =========================

background = pygame.image.load(
    r"programacao\interface\assets\fundos\background_batalha.png"
).convert()



# =========================
# PERSONAGENS
# =========================

nomes_personagens = [
    "Amara",
    "Antonius",
    "Nicholas",
    "Perfidia",
    "Raoni",
    "Taina"
]



def carregar_personagem(nome, direcao):

    imagem = pygame.image.load(
        fr"programacao\interface\assets\personagens\{nome}\rotations\{direcao}.png"
    ).convert_alpha()


    imagem = pygame.transform.scale(
        imagem,
        (
            imagem.get_width()*3,
            imagem.get_height()*3
        )
    )


    return imagem



# =========================
# BARRA DE VIDA
# =========================

def desenhar_barra(x,y,vida,max_vida):

    largura = 250
    altura = 20


    pygame.draw.rect(
        screen,
        VERMELHO,
        (x,y,largura,altura)
    )


    vida_atual = largura * (vida/max_vida)


    pygame.draw.rect(
        screen,
        VERDE,
        (x,y,vida_atual,altura)
    )



# =========================
# BATALHA
# =========================

def main(personagem):


    # escolhe inimigo
    inimigo = random.choice(
        [
            nome
            for nome in nomes_personagens
            if nome != personagem
        ]
    )


    # carrega imagens
    imagem_personagem = carregar_personagem(
        personagem,
        "east"
    )


    imagem_inimigo = carregar_personagem(
        inimigo,
        "west"
    )


    # vida
    hp_player = 120
    hp_enemy = 180


    turno = "player"


    opcoes = [
        "Ataque",
        "Habilidade 1",
        "Habilidade 2",
        "Habilidade 3"
    ]


    selecionado = 0


    mensagem = "A batalha começou!"



    rodando = True


    while rodando:


        # =========================
        # EVENTOS
        # =========================

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                return



            if turno == "player":


                if event.type == pygame.KEYDOWN:


                    if event.key == pygame.K_UP:

                        selecionado = (selecionado-1)%4



                    elif event.key == pygame.K_DOWN:

                        selecionado = (selecionado+1)%4



                    elif event.key == pygame.K_RETURN:


                        if selecionado == 0:

                            dano = random.randint(10,18)


                        elif selecionado == 1:

                            dano = random.randint(18,28)


                        elif selecionado == 2:

                            dano = random.randint(25,35)


                        else:

                            dano = random.randint(35,50)



                        hp_enemy -= dano


                        mensagem = (
                            f"{personagem} causou {dano} de dano!"
                        )


                        turno = "enemy"



        # =========================
        # TURNO INIMIGO
        # =========================

        if turno == "enemy" and hp_enemy > 0:


            pygame.time.delay(500)


            dano = random.randint(8,15)


            hp_player -= dano


            mensagem = (
                f"{inimigo} atacou! ({dano})"
            )


            turno = "player"



        # =========================
        # FIM
        # =========================

        if hp_enemy <= 0:

            hp_enemy = 0

            mensagem = "VOCÊ VENCEU!"

            turno = "fim"



        if hp_player <= 0:

            hp_player = 0

            mensagem = "VOCÊ PERDEU!"

            turno = "fim"



        # =========================
        # DESENHO
        # =========================

        screen.blit(
            background,
            (0,-150)
        )


        # nomes

        screen.blit(
            fonte_titulo.render(
                personagem,
                True,
                BRANCO
            ),
            (175,180)
        )


        screen.blit(
            fonte_titulo.render(
                inimigo,
                True,
                BRANCO
            ),
            (970,180)
        )


        # barras

        desenhar_barra(
            100,
            130,
            hp_player,
            120
        )


        desenhar_barra(
            900,
            130,
            hp_enemy,
            180
        )


        # HP texto

        screen.blit(
            fonte.render(
                f"HP {hp_player}/120",
                True,
                BRANCO
            ),
            (165,155)
        )


        screen.blit(
            fonte.render(
                f"HP {hp_enemy}/180",
                True,
                BRANCO
            ),
            (960,155)
        )



        # personagens

        screen.blit(
            imagem_personagem,
            (50,150)
        )


        screen.blit(
            imagem_inimigo,
            (840,150)
        )



        # menu

        pygame.draw.rect(
            screen,
            PRETO,
            (0,540,1280,180)
        )


        screen.blit(
            fonte.render(
                mensagem,
                True,
                BRANCO
            ),
            (40,555)
        )



        for i,opcao in enumerate(opcoes):

            cor = BRANCO


            if i == selecionado and turno == "player":

                cor = AMARELO



            texto = fonte.render(
                opcao,
                True,
                cor
            )


            screen.blit(
                texto,
                (50,600+i*30)
            )



        pygame.display.flip()


        clock.tick(60)




if __name__ == "__main__":

    main("Amara")