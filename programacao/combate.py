"""
combate.py

Responsável pelo sistema de batalha.

Funções principais:
    - Controle de turnos
    - Aplicação de habilidades
    - Aplicação de efeitos
    - Verificação de vitória
"""

from personagens import personagens as skill
import random
import pygame


# ------------------------
#      Base da tela
# ------------------------

pygame.init()

tela = pygame.display.set_mode((1280, 720)) # criação da tela
pygame.display.set_caption("Terceira Lua")

fonte = pygame.font.SysFont("arial", 32) # criação de uma fonte de texto

# ------------------------
#          Funções
# ------------------------

def criar_combatente(personagem):

    """
    Cria uma cópia temporária de um personagem
    para ser utilizada durante uma batalha.

    """
    combatente = personagem.copy()

    combatente["vida_maxima"] = combatente["vida"]

    combatente["pode_agir"] = True

    combatente["veneno"] = 0
    combatente["cego"] = 0

    combatente["precisao_bonus"] = 0
    combatente["evasao_bonus"] = 0

    combatente["dano_porcentagem"] = 0
    combatente["cura_porcentagem"] = 0

    combatente["dano_pontos"] = 0
    combatente["cura_pontos"] = 0

    return combatente

# ------------------------
#          Botões
# ------------------------

botao1 = pygame.Rect(100, 500, 200, 80)  #criação de um retangulo imaginário
botao2 = pygame.Rect(300, 500, 200, 80)
botao3 = pygame.Rect(550, 500, 200, 80)
botaointeracao = pygame.Rect(800, 500, 250, 80)


pygame.draw.rect(tela, (255, 255, 255) , botao1) #desenho desse retangulo
pygame.draw.rect(tela, (255, 255, 255) , botao2)
pygame.draw.rect(tela, (255, 255, 255) , botao3)
pygame.draw.rect(tela, (255, 255, 255) , botaointeracao)

texto1 = fonte.render("Habilidade 1", True, (0, 0, 0)) #criação de um texto
texto2 = fonte.render("Habilidade 2", True, (0, 0, 0))
texto3 = fonte.render("Habilidade 3", True, (0, 0, 0))
textointeracao = fonte.render("Interações", True, (0, 0, 0))

tela.blit(texto1, (110,520)) #aplicação desse texto
tela.blit(texto2, (330,520))
tela.blit(texto3, (580,520))
tela.blit(textointeracao, (830,520))

# ------------------------
#        Variáveis
# ------------------------

escolha1 = 'Amara' #escolha que acontece em outra área
escolha2 = 'Perfídia'

personagem1 = criar_combatente(skill[escolha1]) #personagem que vai ser utilizado
personagem2 = criar_combatente(skill[escolha2])

qualturno = random.choice([True, False]) #qual personagem começa

# ------------------------
#         Combate
# ------------------------

while personagem1['vida'] > 0 and personagem2['vida'] > 0:
    for evento in pygame.event.get(): # ler o que o mouse faz
        if qualturno: #dizer quem vai agir
            if personagem1['pode_agir']:
                jogador = personagem1
                alvo = personagem2
        else:
            if personagem2['pode_agir']:
                jogador = personagem2
                alvo = personagem1

        # botoes sendo clicados

        if evento.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if botao1.collidepoint(mouse):
                jogador["habilidade_1"](jogador, alvo)
            if botao2.collidepoint(mouse):
                jogador["habilidade_2"](jogador, alvo)
            if botao3.collidepoint(mouse):
                jogador["habilidade_3"](jogador, alvo)
            if botaointeracao.collidepoint(mouse):
                jogador["interações"](jogador, alvo)
        
        # preparo para o próximo turno

        if qualturno:
            personagem1['pode_agir'] = True
        else:
            personagem2['pode_agir'] = True
        qualturno = not qualturno
        qntturno += 1

        #### redesenhar os graficos e botões

        botao1 = pygame.Rect(100, 500, 200, 80)  #criação de um retangulo imaginário
        botao2 = pygame.Rect(300, 500, 200, 80)
        botao3 = pygame.Rect(550, 500, 200, 80)
        botaointeracao = pygame.Rect(800, 500, 250, 80)


        pygame.draw.rect(tela, (255, 255, 255) , botao1) #desenho desse retangulo
        pygame.draw.rect(tela, (255, 255, 255) , botao2)
        pygame.draw.rect(tela, (255, 255, 255) , botao3)
        pygame.draw.rect(tela, (255, 255, 255) , botaointeracao)

        texto1 = fonte.render("Habilidade 1", True, (0, 0, 0)) #criação de um texto
        texto2 = fonte.render("Habilidade 2", True, (0, 0, 0))
        texto3 = fonte.render("Habilidade 3", True, (0, 0, 0))
        textointeracao = fonte.render("Interações", True, (0, 0, 0))

        tela.blit(texto1, (110,520)) #aplicação desse texto
        tela.blit(texto2, (330,520))
        tela.blit(texto3, (580,520))
        tela.blit(textointeracao, (830,520))

        pygame.display.flip()




        

