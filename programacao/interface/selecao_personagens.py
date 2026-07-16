import pygame
from pathlib import Path
from dados_personagens import habilidades

BASE_DIR = Path(__file__).parent

relogio = pygame.time.Clock()

largura, altura = 1280, 720

CINZA = (100, 100, 100, 180)
BRANCO = (255, 255, 255)
# Tupla com cores utilizadas na interface

# As cores são representadas pelo padrão RGB.
# O quarto valor presente em CINZA representa transparência (Alpha),
# utilizado quando uma superfície aceita transparência.


# Configuração da animação
num_personagens = 6
frame = 0
ultimo_tempo = 0

# frame guarda qual imagem da animação está sendo exibida.
# ultimo_tempo registra o momento da última troca de frame.
# A animação utiliza esses valores para controlar a velocidade.


personagem_escolhido = None

# Armazena o personagem selecionado pelo jogador.
# Inicia como None pois nenhum personagem foi escolhido ainda.



def main():
    global frame, ultimo_tempo

    # Função principal responsável por iniciar a tela de seleção
    # e controlar toda a interação do jogador.


    pygame.init()

    # Inicializa todos os módulos do Pygame.



    screen = pygame.display.set_mode((largura, altura))

    # Cria a janela principal onde todos os elementos serão desenhados.



    frame_icons = []

    # Lista que armazenará os ícones dos personagens.



    for i in range(6):

        frame_icon = pygame.image.load(BASE_DIR / "assets" / "frame_selecao.png").convert_alpha()

        # Carrega a moldura utilizada para representar cada personagem.
        # convert_alpha() mantém a transparência da imagem.



        frame_icon = pygame.transform.scale(
            frame_icon,
            (
                int(frame_icon.get_width() * 0.5),
                int(frame_icon.get_height() * 0.5)
            )
        )

        # Redimensiona a imagem para metade do tamanho original.
        # get_width() e get_height() retornam as dimensões atuais da imagem.



        frame_icons.append(frame_icon)

        # Adiciona o frame redimensionado na lista de ícones.



    frame_icons_rect = []

    # Lista que armazenará os Rects dos ícones.
    # Rect controla posição, tamanho e permite colisões.



    for icon in frame_icons:
        frame_icons_rect.append(icon.get_rect())

    # Cria um Rect para cada ícone.



    def desenhar_texto(surface, texto, fonte, cor, x, y, largura_max):

        """
        Desenha um texto quebrando automaticamente em várias linhas
        quando ultrapassa o limite de largura definido.

        Args:
            surface (pygame.Surface): Superfície onde o texto será desenhado.
            texto (str): Texto que será exibido na tela.
            fonte (pygame.font.Font): Fonte utilizada para renderizar o texto.
            cor (tuple): Cor do texto no formato RGB.
            x (int): Posição horizontal inicial do texto.
            y (int): Posição vertical inicial do texto.
            largura_max (int): Limite máximo de largura que uma linha pode ocupar.
        """

        palavras = texto.split()

        # Divide o texto em uma lista de palavras.



        linha = ""

        # Guarda temporariamente as palavras que cabem na linha atual.



        for palavra in palavras:

            teste = linha + palavra + " "

            # Cria uma simulação da próxima linha adicionando a nova palavra.



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

        # Renderiza a última linha restante.



    def carregar_rotacoes(pasta):

        """
        Carrega todas as imagens de rotação de um personagem.

        Args:
            pasta (Path): Caminho da pasta onde estão armazenadas
            as imagens de rotação do personagem.

        Returns:
            list: Lista contendo as imagens das oito direções.
        """

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

        # Retorna uma lista contendo as imagens carregadas.
        # Cada imagem representa uma direção diferente do personagem.



    nomes_personagens = [
        "Amara",
        "Antonius",
        "Nicholas",
        "Perfidia",
        "Raoni",
        "Taina"
    ]

    # Lista contendo os nomes dos personagens disponíveis.



    descricoes = []

    # Lista que armazenará as descrições carregadas dos arquivos .md.



    frame_personagens = [
        carregar_rotacoes(
            BASE_DIR / "assets" / "personagens" / nome / "rotations"
        )
        for nome in nomes_personagens
    ]

    # Carrega as oito animações de cada personagem.
    # Cada posição da lista representa um personagem diferente.



    for nome in nomes_personagens:

        with open(
            BASE_DIR / "assets" / "personagens" / nome / "descricao.md",
            encoding="utf-8"
        ) as arquivo:

            descricoes.append(arquivo.read())

    # Abre o arquivo de descrição de cada personagem
    # e adiciona seu conteúdo na lista descricoes.

        # Cria os retângulos dos personagens
    frame_personagens_rect = []

    # Lista que armazenará os Rects responsáveis pela posição
    # de cada personagem na tela.



    for personagem in frame_personagens:

        frame_personagens_rect.append(personagem[0].get_rect())

    # Cria um Rect utilizando a primeira imagem de cada personagem.
    # Como todas as rotações possuem o mesmo tamanho, qualquer uma delas
    # pode ser utilizada como referência.



    # Cria o painel de seleção

    frame_selecao_rect = pygame.Rect(0, 0, 400, 720)

    # Cria um retângulo que representa a área do painel esquerdo.
    # pygame.Rect recebe posição X, posição Y, largura e altura.



    frame_selecao_surface = pygame.Surface(
        frame_selecao_rect.size,
        pygame.SRCALPHA
    )

    # Cria uma superfície onde o painel será desenhado.
    # SRCALPHA permite que essa superfície tenha transparência.



    frame_selecao_surface.fill(CINZA)

    # Preenche a superfície com a cor definida anteriormente.



    # Cria o painel de descrição

    frame_descricao_rect = pygame.Rect(880, 0, 400, 720)

    # Cria a área onde serão exibidas as informações do personagem.



    frame_descricao_surface = pygame.Surface(
        frame_descricao_rect.size,
        pygame.SRCALPHA
    )

    # Cria uma superfície transparente para o painel de descrição.



    frame_descricao_surface.fill(CINZA)

    # Aplica a cor cinza transparente ao painel.



    background = pygame.image.load(
        BASE_DIR / "assets" / "fundos" / "background_selecao_personagens.png"
    ).convert()

    # Carrega o plano de fundo da tela de seleção.
    # convert() adapta a imagem para o mesmo formato da tela,
    # melhorando o desempenho do desenho.



    posicoes = [
        (70, 140),
        (190, 140),
        (70, 280),
        (190, 280),
        (70, 420),
        (190, 420),
    ]

    # Define as posições onde cada personagem será exibido.



    for rect, pos in zip(frame_personagens_rect, posicoes):

        rect.topleft = pos

    # Associa cada personagem a uma posição.
    # zip() permite percorrer duas listas ao mesmo tempo.



    for rect, (x, y) in zip(frame_icons_rect, posicoes):

        rect.topleft = (x + 4, y + 4)

    # Posiciona os frames de seleção levemente deslocados
    # em relação aos personagens.



    fonte_nome = pygame.font.SysFont("Arial", 48)

    # Fonte utilizada para mostrar o nome do personagem selecionado.



    fonte_habilidade = pygame.font.SysFont("Arial", 32)

    # Fonte utilizada para exibir o título "Habilidades".



    fonte_descricao = pygame.font.SysFont("Arial", 24)

    # Fonte utilizada para mostrar a descrição do personagem.



    running = True

    # Controla o loop principal da tela.
    # Enquanto for True, a tela continua funcionando.



    while running:

        # Obtém a posição atual do mouse.

        mouse_pos = pygame.mouse.get_pos()

        # Retorna uma tupla contendo a posição X e Y do mouse.
        # Essa posição será usada para detectar quando o jogador
        # passa o cursor sobre um personagem.



        for event in pygame.event.get():

            # Captura todos os eventos ocorridos desde o último frame.


            if event.type == pygame.QUIT:

                running = False

            # Fecha a tela caso o jogador clique no botão de fechar.



            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                # Verifica se ocorreu um clique utilizando o botão esquerdo do mouse.



                for i in range(6):

                    if frame_icons_rect[i].collidepoint(event.pos):

                        personagem_escolhido = nomes_personagens[i]

                        running = False

                # Percorre os personagens verificando em qual frame
                # ocorreu o clique.
                # Caso encontre, salva o nome do personagem escolhido
                # e encerra a seleção.



        screen.blit(background, (0, 0))

        # Desenha o plano de fundo da tela.



        screen.blit(
            frame_selecao_surface,
            frame_selecao_rect.topleft
        )

        # Desenha o painel esquerdo de seleção.



        screen.blit(
            frame_descricao_surface,
            frame_descricao_rect.topleft
        )

        # Desenha o painel direito de descrição.



        agora = pygame.time.get_ticks()

        # Retorna o tempo atual do Pygame em milissegundos.
        # É utilizado para controlar a velocidade da animação.



        if agora - ultimo_tempo > 120:

            frame = (frame + 1) % 8

            ultimo_tempo = agora

        # Troca o frame da animação a cada 120 milissegundos.
        # O operador % garante que, ao chegar no último frame,
        # a animação volte para o primeiro.



        screen.blit(
            frame_personagens[0][frame],
            frame_personagens_rect[0]
        )

        # Exibe a animação do primeiro personagem.
        # Esse desenho é substituído posteriormente pelo desenho
        # de todos os personagens voltados para a mesma direção.



        for i in range(6):

            screen.blit(
                frame_icons[i],
                frame_icons_rect[i]
            )

        # Desenha os seis frames de seleção.



        for personagem, rect in zip(
            frame_personagens,
            frame_personagens_rect
        ):

            screen.blit(
                personagem[4],
                rect
            )

        # Desenha todos os personagens utilizando a rotação "south".
        # O índice 4 corresponde à direção sul na lista de rotações.

                # Exibe uma versão ampliada do personagem ao passar o mouse

        for i in range(6):

            if frame_icons_rect[i].collidepoint(mouse_pos):

                # Verifica se o mouse está dentro do Rect de algum personagem.
                # collidepoint() retorna True quando uma posição está dentro
                # dos limites de um Rect.



                personagem = frame_personagens[i][frame]

                # Pega o frame atual da animação do personagem que está
                # sendo observado pelo mouse.



                personagem = pygame.transform.scale(
                    personagem,
                    (
                        int(personagem.get_width() * 4),
                        int(personagem.get_height() * 4)
                    )
                )

                # Aumenta o tamanho do personagem para destacá-lo na tela.
                # O tamanho original é multiplicado por 4.



                rect = personagem.get_rect(
                    center=(largura // 2, altura // 2 + 50)
                )

                # Cria um novo Rect para o personagem ampliado.
                # center posiciona a imagem pelo centro da tela.
                # // realiza uma divisão inteira, retornando apenas o valor inteiro.



                texto_nome_personagem = fonte_nome.render(
                    nomes_personagens[i],
                    True,
                    BRANCO
                )

                # Transforma o nome do personagem em uma imagem renderizada.
                # O segundo parâmetro ativa o antialiasing para suavizar o texto.



                screen.blit(
                    texto_nome_personagem,
                    (1010, 40)
                )

                # Desenha o nome do personagem no painel de descrição.



                desenhar_texto(
                    screen,
                    descricoes[i],
                    fonte_descricao,
                    BRANCO,
                    900,
                    120,
                    350
                )

                # Exibe a descrição do personagem.
                # A função desenhar_texto realiza a quebra automática
                # das linhas para que o texto permaneça dentro do painel.



                screen.blit(personagem, rect)

                # Desenha o personagem ampliado na tela.



                # Exibição das habilidades

                nome = nomes_personagens[i]

                # Guarda o nome do personagem atual.
                # Será utilizado para buscar suas habilidades no dicionário.



                texto_habilidades = fonte_habilidade.render(
                    "Habilidades:",
                    True,
                    BRANCO
                )

                # Cria o texto do título da seção de habilidades.



                screen.blit(
                    texto_habilidades,
                    (900, 400)
                )

                # Desenha o título das habilidades no painel direito.



                y = 450

                # Define a posição vertical inicial onde as habilidades
                # serão desenhadas.



                for habilidade in habilidades[nome]:

                    texto = fonte_descricao.render(
                        habilidade,
                        True,
                        BRANCO
                    )

                    # Renderiza cada habilidade individualmente.



                    screen.blit(
                        texto,
                        (900, y)
                    )

                    # Desenha a habilidade na posição definida.



                    y += 30

                    # Move a próxima habilidade para baixo,
                    # evitando que os textos fiquem sobrepostos.



        pygame.display.flip()

        # Atualiza a tela mostrando tudo que foi desenhado no frame atual.



        relogio.tick(60)

        # Limita o jogo para 60 FPS.
        # Evita que a velocidade da animação dependa do computador.



    return personagem_escolhido

    # Retorna o nome do personagem escolhido pelo jogador.
    # Esse valor é recebido posteriormente pela tela de batalha.



if __name__ == "__main__":

    main()

    # Verifica se esse arquivo foi executado diretamente.
    # Caso seja, inicia a função principal.


# Auxílio da inteligência artificial utilizado para a criação do GIF
# e para ajustar o comportamento dos textos dentro das caixas.