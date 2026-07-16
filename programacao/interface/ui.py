import pygame

# Pygame é o responsavel pelo visual, interações, sons do jogo.

import webbrowser

# Para a criação de um link clicável.
# Nesse projeto só é usado uma vez para o linkedin.

from pathlib import Path

# Pathlib foi usado para facilitar o gerenciamento de caminho de arquivos para que funcione em qualquer lugar.

BASE_DIR = Path(__file__).parent

# __file__ representa o caminho do arquivo Python que está sendo executado.
# Path() transforma esse caminho em um objeto manipulável.
# .parent retorna a pasta onde esse arquivo está localizado.
# Nesse caso, retorna a pasta interface.
# Algumas vezes, será necessário utilizar .parent novamente, retornando a pasta programacao.


def main():

    # Função principal, responsável por iniciar o pygame.

    pygame.init()

    # Inicia todos os módulos do Pygame.
    # Se qualquer comando de Pygame vier antes disso, há grandes chances de não funcionar.

    pygame.mixer.music.load(BASE_DIR.parent / "soundtrack" / "Batalha_das_Luas.mp3")

    # pygame.mixer.music é o módulo responsável pela reprodução de músicas.
    # BASE_DIR.parent Volta uma pasta para acessar a pasta soundtrack.

    pygame.mixer.music.play(-1)

    # Inicia a reprodução da música.
    # O valor -1 faz com que ela fique repetindo infinitamente.

    largura, altura = 1280, 720
    
    # Tamanho da tela

    screen = pygame.display.set_mode((largura, altura))

    # Cria a janela principal do jogo.
    # screen representa a área onde todos os elementos visuais serão desenhados.

    pygame.display.set_caption("Menu")

    # Define o nome da janela.

    relogio = pygame.time.Clock()

    # Cria um controlador de tempo do Pygame.
    # Ele será utilizado depois para limitar a quantidade de FPS do jogo.

    background = pygame.image.load(BASE_DIR / "assets" / "fundos" / "background.png").convert()

    # Carrega a imagem utilizada como fundo do menu.

    # O convert() adapta a imagem para o mesmo formato utilizado pela tela,
    # melhorando o desempenho na hora de desenhar.

    logo = pygame.image.load(BASE_DIR / "terceira lua png.png").convert_alpha()

    # Logo Terceira lua

    # convert_alpha() é usado porque a imagem possui transparência.
    # Ele mantém o canal Alpha, permitindo que partes transparentes continuem invisíveis.

    logo = pygame.transform.scale(logo,(int(logo.get_width() * 0.6), int(logo.get_height() * 0.6)))

    # Redimensiona a logo para 60% do tamanho original.

    # get_width() e get_height() retornam o tamanho atual da imagem.

    logo_rect = logo.get_rect(center=(largura / 2, (altura / 2) - 150))

    # Cria um retângulo que representa a posição e o tamanho da logo.
    # O Rect é utilizado pelo Pygame para controlar localização dos elemento e também permite realizar colisões.
    
    # center define que a imagem será posicionada pelo centro,
    # ao invés do canto superior esquerdo(que é o padrão).

    moldura = pygame.image.load(
        BASE_DIR / "assets" / "ai-made" / "menu_frame.png"
    )
    # Imagem moldura

    moldura = pygame.transform.scale(moldura,(moldura.get_width() * 2.5, moldura.get_height() * 2.5))
    # Redimensiona a moldura 

    moldura_rect = moldura.get_rect(center=(largura / 2, (altura / 2) + 150))
    # Cria o Rect responsável por controlar a posição do moldura.
    # O moldura é centralizado horizontalmente e deslocado para baixo
    # utilizando o valor +150 no eixo Y.

    botao_jogar = pygame.image.load(BASE_DIR / "assets" / "ai-made" / "jogar_button.png").convert_alpha()
    # Imagem botão jogar

    botao_jogar = pygame.transform.scale(botao_jogar,(botao_jogar.get_width() * 2.4, botao_jogar.get_height() * 2.4))
    # Redimensiona o botão Jogar

    botao_jogar_rect = botao_jogar.get_rect(center=(moldura_rect.centerx, moldura_rect.centery - 74))
    # Posiciona o botão utilizando o centro do moldura como referência.

    # centerx representa a posição central horizontal do moldura.
    # centery representa a posição central vertical.

    # O valor -74 desloca o botão para cima dentro do moldura.

    botao_sair = pygame.image.load(BASE_DIR / "assets" / "ai-made" / "sair_button.png").convert_alpha()
    # Imagem botão sair

    botao_sair = pygame.transform.scale(botao_sair,(botao_sair.get_width() * 2.4, botao_sair.get_height() * 2.4))
    # Redimensiona o botão Sair

    botao_sair_rect = botao_sair.get_rect(center=(moldura_rect.centerx, moldura_rect.centery - 8))
    # Posição do botão Sair

    fonte_creditos = pygame.font.SysFont(None, 22)
    # Cria a fonte utilizada para escrever os créditos na tela.
    # O primeiro parâmetro define a fonte utilizada.
    # None significa que será utilizada a fonte padrão do sistema.
    # O valor 22 representa o tamanho da fonte.

    link = "https://www.linkedin.com/in/yasmin-pereira-lucas"
    # Armazena o endereço do LinkedIn que será aberto ao clicar no texto dos créditos.

    link_rect = None
    # Variável que irá armazenar o Rect do texto do LinkedIn.
    # Ela começa como None porque o texto ainda não foi desenhado na tela.
    # Depois será utilizada para detectar se o jogador clicou sobre o link.

    running = True
    # Controla o loop principal
    # Enquanto running for True, o jogo continua funcionando.
    # Quando receber False, o loop é encerrado.
    while running:

        # Processa os eventos
        for event in pygame.event.get():
        # Captura todos os eventos que aconteceram desde o último frame.
        # Seja esses eventos clicks do mouse, teclas do teclado pressionadas, etc.

            if event.type == pygame.QUIT:
                running = False
            # Verifica se o jogador fechou a janela pelo botão "X".
            # Caso aconteça, altera running para False e encerra o menu.

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Clique do mouse

                if event.button == 1:
                    # Botão esquerdo do mouse

                    if link_rect and link_rect.collidepoint(event.pos):
                        # Verifica se o clique aconteceu dentro da área do texto do LinkedIn.
                        # collidepoint() verifica se uma posição está dentro de um Rect.

                        webbrowser.open(link)

                        # Abre o link do LinkedIn no navegador padrão.


                    if botao_sair_rect.collidepoint(event.pos):
                        # Verifica se o clique aconteceu dentro da área do botão Sair.
                        # Caso aconteça, encerra o loop principal.

                        running = False



                    if botao_jogar_rect.collidepoint(event.pos):
                    # Verifica se o clique aconteceu dentro da área do botão Jogar.
                    # Caso aconteça, abre a tela de seleção de personagens.

                        from interface import selecao_personagens
                        from interface import tela_batalha
                        # Importa as telas necessárias somente quando o botão Jogar for pressionado.


                        personagem = selecao_personagens.main()
                        # Executa a tela de seleção de personagens.
                        # Após a escolha do jogador, a função retorna o nome do personagem escolhido.


                        if personagem is not None:
                            # Verifica se algum personagem foi selecionado.
                            # Caso exista um personagem válido, inicia a batalha.

                            tela_batalha.main(personagem)


                        running = False

                        # Encerra o menu após iniciar a próxima tela.


        screen.blit(background, (0, 0))
        # Desenha o background na tela.
        # blit() copia uma imagem para dentro da superfície principal do jogo.
        # O segundo parâmetro define a posição onde ela será desenhada.

        screen.blit(logo, logo_rect)
        # Desenha a logo utilizando o Rect criado anteriormente para definir sua posição.

        screen.blit(moldura, moldura_rect)
        # Desenha a moldura

        screen.blit(botao_jogar, botao_jogar_rect)
        # Desenha o botão Jogar

        screen.blit(botao_sair, botao_sair_rect)
        # Desenha o botão Sair

        creditos = [
            "Trilha Sonora: Batalha das Luas",
            "Composição: Yasmin Pereira Lucas",
            "LinkedIn: linkedin.com/in/yasmin-pereira-lucas",
            "Todos os direitos reservados."
        ]
        # Lista contendo os textos que serão exibidos na parte dos créditos.

        y = altura - 90
        # Define a posição inicial vertical dos créditos.
        # O valor é calculado a partir da altura da tela para manter os textos próximos à parte inferior.

        mouse = pygame.mouse.get_pos()
        # Obtém a posição atual do mouse.
        # Será utilizado para verificar quando o cursor está sobre o LinkedIn.

        for linha in creditos:
        # Percorre cada linha da lista de créditos para renderizar o texto.

            if linha.startswith("LinkedIn"):
            # Verifica se a linha atual começa com "LinkedIn".
            # Essa condição é usada para aplicar um comportamento diferente somente ao texto do link.

                if link_rect and link_rect.collidepoint(mouse):
                    # Altera a cor do LinkedIn quando o mouse está sobre ele,
                    # criando um efeito visual de destaque.

                    cor = (120, 200, 255)
                else:
                    cor = (80, 160, 255)

            else:
                cor = (255, 255, 255)
                # Cor padrão dos créditos

                
            

            texto = fonte_creditos.render(linha, True, cor)
            # Renderiza o texto transformando uma string em uma imagem que pode ser desenhada na tela.
            # O primeiro parâmetro é o texto que será exibido.
            # O segundo parâmetro ativa o antialiasing, deixando as letras mais suaves.
            # O terceiro parâmetro define a cor do texto.

            rect = texto.get_rect(topleft=(20, y))
            # Cria um Rect para controlar a posição do texto.
            # topleft define que a posição informada será o canto superior esquerdo.

            screen.blit(texto, rect)
            # Desenha o texto dos créditos na tela.

            if linha.startswith("LinkedIn"):
                # Guarda a posição do texto do LinkedIn.
                # Esse Rect será usado para detectar quando o jogador clicar no link.
                
                link_rect = rect

            y += 18
            # Aumenta a posição vertical para que a próxima linha seja desenhada abaixo da anterior.

        pygame.display.flip()
        # Atualiza a tela mostrando tudo que foi desenhado durante esse frame.
        # O Pygame primeiro desenha os elementos e depois exibe as alterações.
        # Sem isso nada seria desenhado

        relogio.tick(60)
        # Limita a execução do loop para 60 frames por segundo.
        # Isso evita que o jogo rode em velocidades diferentes dependendo do computador.

    pygame.quit()
    # Encerra os módulos do Pygame e libera os recursos utilizados.

if __name__ == "__main__":
    main()
# Verifica se este arquivo foi executado diretamente.
# Caso seja, chama a função principal do programa.

# A inteligência artificial foi utilizada como ferramenta de apoio durante o aprendizado do Pygame.