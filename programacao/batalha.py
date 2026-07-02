# ===============================================
#     1- DEFININDO OS ESTADOS DA BATABLHA 
# ===============================================
''' Primeiro vou usar a biblioteca nativa enum do Python para mapear exatamente o que está 
acontecendo no jogo. Isso evita variáveis soltas'''

from enum import Enum, auto

class EstadoBatalha(Enum):
    INICIO_BATALHA = auto()      # Carrega personagens, aplica passivas iniciais
    TURNO_JOGADOR = auto()       # Aguarda o input da interface 
    TURNO_BOT = auto()           # Momento em que a IA decide a ação
    PROCESSANDO_ACAO = auto()    # Calcula dano/efeitos 
    FIM_BATALHA = auto()         # Alguém morreu, define vitória/derrota e avança campanha

# ==================================================
#     2- ESTRUTUTURA DO GERENCIADOR DE BATALHA
# ==================================================
''' Vou criar a classe principal que vai ser controlada.
    Ela vai ditar o ritmo do jogo.'''

class GerenciadorBatalha:
    def __init__(self, jogador, bot):
        self.jogador = jogador  # Objeto do personagem do jogador (vindo do JSON)
        self.bot = bot          # Objeto do bot (vindo do JSON)
        self.estado_atual = EstadoBatalha.INICIO_BATALHA
        self.turno_atual = 1
        self.quem_joga = "Jogador"  # Quem começa (pode ser decidido por velocidade/sorte)

    def iniciar_combate(self):
        """Prepara o terreno para a luta começar."""
        print(f"--- Iniciando Batalha: {self.jogador['nome']} VS {self.bot['nome']} ---")
        # TODO: Chamar função do Gabriel para aplicar passivas de início de jogo
        
        # Define quem começa e muda o estado
        if self.quem_joga == "Jogador":
            self.estado_atual = EstadoBatalha.TURNO_JOGADOR
        else:
            self.estado_atual = EstadoBatalha.TURNO_BOT
            
        self.atualizar_loop()

    def atualizar_loop(self):
        """O coração do sistema. Controla o fluxo baseado no estado atual."""
        if self.estado_atual == EstadoBatalha.TURNO_JOGADOR:
            print(f"\n[Turno {self.turno_atual}] Sua vez! Escolha uma habilidade...")
            # Aqui o código para, esperando o Luiz (Interface) enviar a escolha.
            
        elif self.estado_atual == EstadoBatalha.TURNO_BOT:
            print(f"\n[Turno {self.turno_atual}] Vez do Bot pensando...")
            self.executar_turno_bot()

    def executar_turno_bot(self):
        """Chama a lógica da IA (que eu vou desenvolver depois)."""
        # Exemplo simples temporário: o bot sempre usa a habilidade 1
        habilidade_escolhida = "habilidade1" 
        
        # Avançando para processar a ação do bot
        self.processar_acao(temporario_autor="Bot", habilidade=habilidade_escolhida)

    def processar_acao(self, autor, habilidade):
        """Aplica os efeitos da jogada, atualiza cooldowns e checa vida."""
        self.estado_atual = EstadoBatalha.PROCESSANDO_ACAO
        print(f"> {autor} usou {habilidade}!")
        
        # TODO: Aqui eu vou integrar com o sistema de dano do Gabriel/Rafael.
        # Exemplo simulado:
        if autor == "Bot":
            self.jogador["vida_atual"] -= 15  # Simulação de dano
        else:
            self.bot["vida_atual"] -= 20

        # 1. Diminuir o cooldown das habilidades desse personagem
        # 2. Processar ticks de veneno/sangramento (Buffs/Debuffs)

        # Checa se o jogo acabou
        if self.checar_fim_de_jogo():
            self.estado_atual = EstadoBatalha.FIM_BATALHA
            self.finalizar_batalha()
        else:
            # Se ninguém morreu, passa o turno
            self.passar_turno()

    def passar_turno(self):
        """Alterna quem joga e incrementa o contador de turnos."""
        if self.quem_joga == "Jogador":
            self.quem_joga = "Bot"
            self.estado_atual = EstadoBatalha.TURNO_BOT
        else:
            self.quem_joga = "Jogador"
            self.estado_atual = EstadoBatalha.TURNO_JOGADOR
            self.turno_atual += 1  # O ciclo fecha quando volta para o jogador
            
        self.atualizar_loop()

    def checar_fim_de_jogo(self):
        return self.jogador["vida_atual"] <= 0 or self.bot["vida_atual"] <= 0

    def finalizar_batalha(self):
        if self.jogador["vida_atual"] <= 0:
            print("\n❌ Derrota! O Bot venceu.")
            # TODO: Chamar tela de derrota do Luiz
        else:
            print("\n🏆 Vitória! Você venceu.")
            # TODO: Avançar a campanha (minha responsabilidade) e chamar tela de vitória do Luiz


