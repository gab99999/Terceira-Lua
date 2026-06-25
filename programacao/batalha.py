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
    PROCESSANDO_ACAO = auto()    # Calcula dano/efeitos e atualiza cooldowns
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
        habilidade_escolhida = "habilidade_basica" 
        
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


# ==============================================================================================================================
#                                    GERENCIAMENTO DOS COOLDOWNS E OS EFEITOS
# ==============================================================================================================================
''' Essa parte vai controlar o tempo  no jogo. A regra  principal 
é que o tempo só passa quando o turno muda, então vou decrementar
esses contadores em momento bem específico do fluxo. '''
# ==============================================
#        ETRUTURA DE COOLDOWNS E EFEITOS
# ==============================================
jogador = {
    "nome": "Pyro",
    "vida_atual": 100,
    # Cooldowns: quantas rodadas faltam para poder usar a habilidade de novo
    "cooldowns": {
        "habilidade_basica": 0,
        "habilidade_tematica": 2, # Faltam 2 turnos para poder usar
        "ultimate": 0             # Pronto para usar!
    },
    # Efeitos ativos no personagem neste exato momento
    "efeitos_ativos": [
        {"nome": "envenenamento", "duracao": 3, "valor": 5}, # Dura 3 turnos, tira 5 de vida por turno
        {"nome": "escudo", "duracao": 1, "valor": 20}        # Dura 1 turno, absorve 20 de dano
    ]
}
# Estrutura com esboço de personagem para o Gabriel formatar com as informaçôes dos personagens originais !!!

# ===============================================
#      2- ATUALIZAR NO CONTADOR DE BATALHA 
# ===============================================
''' O melhor momento para atualizar os contadores de um personagem é 
no inicio do turno dele, logo antes de ele escolher a ação.
   Vou usar a antiga função " passar_turno " e criar duas funções 
auxiliares: atualizar_cooldowns e processar_efeitos. '''

def passar_turno(self):
        """Alterna quem joga, avança o contador e atualiza os status do próximo a jogar."""
        if self.quem_joga == "Jogador":
            self.quem_joga = "Bot"
            self.estado_atual = EstadoBatalha.TURNO_BOT
            # O turno agora é do Bot. Vamos atualizar as coisas dele antes de ele agir.
            self.atualizar_status_personagem(self.bot)
        else:
            self.quem_joga = "Jogador"
            self.estado_atual = EstadoBatalha.TURNO_JOGADOR
            self.turno_atual += 1
            # O turno voltou para o Jogador. Vamos atualizar as coisas dele.
            self.atualizar_status_personagem(self.jogador)
            
        self.atualizar_loop()

def atualizar_status_personagem(self, personagem):
    """Reúne as atualizações de tempo que acontecem no início do turno do personagem."""
    print(f"\n--- Atualizando status de: {personagem['nome']} ---")
    self.processar_efeitos(personagem)
    self.atualizar_cooldowns(personagem)

def atualizar_cooldowns(self, personagem):
    """Diminui o tempo de recarga de todas as habilidades que estão em cooldown."""
    for habilidade, tempo_restante in personagem["cooldowns"].items():
        if tempo_restante > 0:
            personagem["cooldowns"][habilidade] -= 1
            if personagem["cooldowns"][habilidade] == 0:
                print(f"✨ A habilidade [{habilidade}] de {personagem['nome']} está pronta para uso novamente!")

def processar_efeitos(self, personagem):
    """Aplica os efeitos temporários (como dano de veneno) e reduz a duração deles."""
    # Usamos uma lista nova para manter apenas os efeitos que não expiraram
    efeitos_restantes = []

    for efeito in personagem["efeitos_ativos"]:
        # 1. Aplica o efeito dependendo do tipo
        if efeito["nome"] == "envenenamento":
            personagem["vida_atual"] -= efeito["valor"]
            print(f"🤢 {personagem['nome']} sofreu {efeito['valor']} de dano por Veneno! (Vida: {personagem['vida_atual']})")
            
        elif efeito["nome"] == "escudo":
            print(f"🛡️ {personagem['nome']} está protegido por um escudo de {efeito['valor']} pontos.")

        # 2. Diminui a duração do efeito
        efeito["duracao"] -= 1

        # 3. Se a duração ainda for maior que zero, o efeito continua para o próximo turno
        if efeito["duracao"] > 0:
                efeitos_restantes = efeito
        else:
            print(f"⏳ O efeito [{efeito['nome']}] em {personagem['nome']} acabou.")

    # Atualiza a lista do personagem apenas com os efeitos que ainda estão ativos
    personagem["efeitos_ativos"] = efeitos_restantes

''' Novamente, é apenas um esboço, não é definitivo. Também, em relação a saída,
pelo fato de ter muitos personagens, eu usei (mas não apliquei ainda) IA para me
ajudar com um print genérico (string formatadas). '''

    
