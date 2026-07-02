import pygame


WIDTH, HEIGHT = 1280, 720


# Cores
CINZA = (128, 128, 128, 150)
BRANCO = (255, 255, 255) 
PRETO = (0, 0, 0) 
VERMELHO = (255, 0, 0) 
AZUL = (0, 0, 255) 
VERDE = (0, 255, 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    frame_selecao_rect = pygame.Rect(100, 50, 100, 100)
    frame_selecao_surface = pygame.Surface(frame_selecao_rect.size, pygame.SRCALPHA)
    frame_selecao_surface.fill(CINZA)
    
    background = pygame.image.load(r"programacao\interface\assets\background_selecao_personagens.png").convert()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        # DESENHO AQUI DENTRO DO LOOP
        screen.blit(background, (0, 0))

        screen.blit(frame_selecao_surface, frame_selecao_rect.topleft)


        pygame.display.flip()


    pygame.quit()

main()