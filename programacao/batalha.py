# motor da batalha por turnos.

# a interface só precisa criar um ``GerenciadorBatalha`` e chamar
# ``executar_acao`` quando o jogador escolher uma habilidade ou interação.


from enum import Enum, auto
import random

from combate import criar_combatente
from eventos import terceira_lua
from interacoes import criar_interacoes, tentar_interacao
from personagens import personagens
from turnos import SistemaTurnos
import base as b


class EstadoBatalha(Enum):
    INICIO_BATALHA = auto()
    TURNO_JOGADOR = auto()
    TURNO_BOT = auto()
    PROCESSANDO_ACAO = auto()
    FIM_BATALHA = auto()


class GerenciadorBatalha:
    """ coordena uma partida sem depender do Pygame.

    ``jogador`` e ``bot`` podem ser os modelos de ``personagens`` ou
    combatentes já criados. ``turno_terceira_lua`` é opcional para permitir
    partidas e testes determinísticos.
    """

    def __init__(self, jogador, bot, turno_terceira_lua=None):
        self.jogador = self._criar_se_necessario(jogador)
        self.bot = self._criar_se_necessario(bot)
        self.turnos = SistemaTurnos(self.jogador, self.bot)
        self.interacoes_restantes = criar_interacoes()
        self.estado_atual = EstadoBatalha.INICIO_BATALHA
        self.turno_atual = 1
        self.turno_terceira_lua = (
            turno_terceira_lua
            if turno_terceira_lua is not None
            else random.randint(9, 12)
        )
        self.terceira_lua_ativa = False
        self.evento_terceira_lua = None
        self.historico = []

    @staticmethod
    def _criar_se_necessario(personagem):
        if isinstance(personagem, str):
            personagem = personagens[personagem]

        if "vida_maxima" in personagem:
            personagem["vida_maxima"] = int(personagem["vida_maxima"])
            personagem["vida"] = int(personagem["vida"])
            return personagem

        combatente = criar_combatente(personagem)

        combatente["vida_maxima"] = int(combatente["vida_maxima"])
        combatente["vida"] = int(combatente["vida"])

        return combatente

    def iniciar_combate(self):
        """ erepara a primeira vez do jogador e devolve o estado inicial"""
        self._registrar(
            f"Batalha iniciada: {self.jogador['nome']} vs {self.bot['nome']}."
        )
        self._iniciar_turno()
        return self.resumo()

    def atualizar_loop(self):
        # ponto de compatibilidade
        return self.resumo()

    def executar_acao(self, acao, interacao=None):
        """ executa a ação do jogador e, em seguida, a resposta do bot

        ``acao`` aceita ``habilidade_1``, ``habilidade_2``, ``habilidade_3``
        ou ``interacao``. Para uma interação, informe a chave em ``interacao``.
        """
        if self.estado_atual != EstadoBatalha.TURNO_JOGADOR:
            raise ValueError("Não é o turno do jogador.")
        self._executar_acao_atual(acao, interacao)
        if not self.checar_fim_de_jogo() and self.estado_atual == EstadoBatalha.TURNO_BOT:
            self.executar_turno_bot()
        return self.resumo()

    def executar_turno_bot(self):
        """ escolhe uma habilidade e executa o turno do bot."""
        if self.estado_atual != EstadoBatalha.TURNO_BOT:
            return self.resumo()
        acao = self._escolher_acao_bot()
        self._executar_acao_atual(acao)
        return self.resumo()

    def _escolher_acao_bot(self):
        # as três habilidades estão sempre prontas.
        opcoes = ("habilidade_1", "habilidade_2", "habilidade_3")
        dificuldade = self.bot.get("dificuldade", "FÁCIL")
        if dificuldade == "MÉDIA":
            return "habilidade_3"
        if dificuldade == "DIFÍCIL" and self.jogador["vida"] <= 150:
            return "habilidade_3"
        return random.choice(opcoes)

    def processar_acao(self, autor, habilidade, interacao=None):
        # gerenciador de ações.
        combatente = self.jogador if autor == "Jogador" else self.bot
        if combatente is not self.turnos.jogador_atual():
            raise ValueError("O autor informado não é o combatente do turno.")
        return self._executar_acao_atual(habilidade, interacao)

    def _executar_acao_atual(self, acao, nome_interacao=None):
        usuario = self.turnos.jogador_atual()
        alvo = self.turnos.alvo_atual()
        self.estado_atual = EstadoBatalha.PROCESSANDO_ACAO

        # aceita também os nomes sem sublinhado usados nos rascunhos da IA.
        acao = {
            "habilidade1": "habilidade_1",
            "habilidade2": "habilidade_2",
            "habilidade3": "habilidade_3",
        }.get(acao, acao)

        vida_usuario_antes = usuario["vida"]
        vida_alvo_antes = alvo["vida"]

        if acao in ("habilidade_1", "habilidade_2", "habilidade_3"):
            usuario[acao](usuario, alvo)
            descricao = acao.replace("_", " ")
            self._acelerar_terceira_lua_se_necessario(
                usuario, acao, vida_alvo_antes, alvo["vida"]
            )
        elif acao == "interacao":
            if not nome_interacao:
                raise ValueError("Informe o nome da interação escolhida.")
            if not tentar_interacao(nome_interacao, self.interacoes_restantes, usuario, alvo):
                raise ValueError("Interação indisponível.")
            descricao = nome_interacao.replace("_", " ")
        else:
            raise ValueError("Ação inválida.")

        b.limitar_vida(usuario)
        b.limitar_vida(alvo)
        dano = max(0, vida_alvo_antes - alvo["vida"])
        cura = max(0, usuario["vida"] - vida_usuario_antes)
        self._registrar(
            f"{usuario['nome']} usou {descricao} "
            f"(dano: {dano:.0f}, cura: {cura:.0f})."
        )

        # Cegueira duração.
        usuario["cego"] = False
        if self.checar_fim_de_jogo():
            self.finalizar_batalha()
            return
        self.passar_turno()

    def _acelerar_terceira_lua_se_necessario(self, usuario, acao, vida_antes, vida_depois):
        # acelaração da perfídia
        if self.terceira_lua_ativa or usuario["nome"] != "Perfídia":
            return
        if vida_depois >= vida_antes:
            return
        if acao == "habilidade_1":
            self.acelerar_terceira_lua(1)
        elif acao == "habilidade_3":
            self.acelerar_terceira_lua(random.randint(1, 2))

    def acelerar_terceira_lua(self, quantidade):
        # prevenção de bugs com a terceira lua
        chegada_anterior = self.turno_terceira_lua
        self.turno_terceira_lua = max(
            self.turno_atual + 1,
            self.turno_terceira_lua - quantidade,
        )
        adiantado = chegada_anterior - self.turno_terceira_lua
        if adiantado:
            self._registrar(
                f"A Perfídia adiantou a Terceira Lua em {adiantado} turno(s)."
            )

    def passar_turno(self):
        self.turnos.proximo_turno()
        if self.turnos.jogador_atual() is self.jogador:
            self.turno_atual += 1
        self._iniciar_turno()

    def _iniciar_turno(self):
        if self.checar_fim_de_jogo():
            self.finalizar_batalha()
            return

        if not self.terceira_lua_ativa and self.turno_atual >= self.turno_terceira_lua:
            self._ativar_terceira_lua()

        usuario = self.turnos.jogador_atual()
        alvo = self.turnos.alvo_atual()
        self._aplicar_passivas_de_turno(usuario, alvo)
        b.limitar_vida(usuario)
        b.limitar_vida(alvo)
        if self.checar_fim_de_jogo():
            self.finalizar_batalha()
            return

        if not usuario["pode_agir"]:
            usuario["pode_agir"] = True
            self._registrar(f"{usuario['nome']} perdeu o turno.")
            self.passar_turno()
            return

        self.estado_atual = (
            EstadoBatalha.TURNO_JOGADOR
            if usuario is self.jogador
            else EstadoBatalha.TURNO_BOT
        )
        self._registrar(f"Turno {self.turno_atual}: vez de {usuario['nome']}.")

    def _aplicar_passivas_de_turno(self, usuario, alvo):
        # executa somente passivas que são realmente de início de turno.
        nome = usuario["nome"]
        if nome in ("Amara", "Antonius", "Tainá"):
            usuario["passiva"](usuario, alvo)

    def _ativar_terceira_lua(self):
        self.terceira_lua_ativa = True
        self.evento_terceira_lua = terceira_lua(self.jogador, self.bot)
        self._registrar(
            f"A Terceira Lua chegou no turno {self.turno_atual} "
            f"(evento {self.evento_terceira_lua})."
        )

        for combatente, outro in ((self.jogador, self.bot), (self.bot, self.jogador)):
            if combatente["nome"] == "Perfídia":
                combatente["terceira_lua"] = True
                combatente["passiva"](combatente, outro)

    def checar_fim_de_jogo(self):
        return self.turnos.combate_acabou()

    def finalizar_batalha(self):
        if self.estado_atual == EstadoBatalha.FIM_BATALHA:
            return
        self.estado_atual = EstadoBatalha.FIM_BATALHA
        vencedor = self.turnos.vencedor()
        self._registrar(f"Fim de batalha: {vencedor['nome']} venceu.")

    def resumo(self):
        """ estado que uma interface pode consultar a cada ação."""
        return {
            "estado": self.estado_atual,
            "turno_atual": self.turno_atual,
            "turno_terceira_lua": self.turno_terceira_lua,
            "terceira_lua_ativa": self.terceira_lua_ativa,
            "evento_terceira_lua": self.evento_terceira_lua,
            "jogador": self.jogador,
            "bot": self.bot,
            "interacoes_disponiveis": tuple(self.interacoes_restantes),
            "historico": tuple(self.historico),
        }

    def _registrar(self, mensagem):
        self.historico.append(mensagem)
