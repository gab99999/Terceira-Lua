# ====================================================
# 2- ESTRUTURANDO OS NÍVEIS DE INTELIGÊNCIA ARTIFICIAL
#                (AUXILIADO POR IA)
# ====================================================
''' Agora eu vou atualizar a função " executar_turno_bot " para 
decidir a ação com base no bot atual. '''

import random

def executar_turno_bot(self):
    print(f"\n🤖 [Turno {self.turno_atual}] O Bot {self.bot['nome']} está decidendo a jogada...")
    
    # 1. Descobre o que o bot pode usar neste turno
    opcoes = self.obter_habilidades_disponiveis(self.bot)
    habilidade_escolhida = "habilidade1" # Padrão de segurança caso algo dê errado
    
    # 2. Define o comportamento baseado na dificuldade do Bot atual
    dificuldade = self.bot.get("dificuldade", "FÁCIL")
    
    if dificuldade == "FÁCIL":
        # IA aleatória: Escolhe qualquer habilidade disponível ao acaso.
        # Ótimo para os primeiros inimigos da campanha!
        habilidade_escolhida = random.choice(opcoes)
        
    elif dificuldade == "MÉDIA":
        # IA Baseada em Regras Simples: Usa a melhor habilidade se puder.
        if "habilidade3" in opcoes:
            habilidade_escolhida = "habilidade3"
        elif "habilidade2" in opcoes:
            habilidade_escolhida = "habilidade2"
        else:
            habilidade_escolhida = "habilidade1"
            
    elif dificuldade == "DIFÍCIL":
        # IA Inteligente: Olha para o próprio status e o do jogador antes de agir.
        habilidade_escolhida = self.logica_ia_avancada(opcoes)

    # 3. Avança o fluxo do jogo passando a escolha para o processador de ações
    self.processar_acao(autor="Bot", habilidade=habilidade_escolhida)

''' AQUI EU USEI IA MAJORITÁRIAMENTE PARA PARTE DA LÓGICA. 
TAMBÉM USEI UMA BASE SINTÁTICA FORNECIDA PELA IA, PARA QUE EU PODESSE
APRENDER A CLASSIFICAR DIFICULDADE E DEPOIS REESCREVER DO MEU JEITO. '''
