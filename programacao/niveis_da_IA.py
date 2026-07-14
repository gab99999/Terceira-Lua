# ====================================================
# 2- ESTRUTURANDO OS NÍVEIS DE INTELIGÊNCIA ARTIFICIAL
#                (AUXILIADO POR IA)
# ====================================================
''' Agora eu vou atualizar a função " executar_turno_bot " para 
decidir a ação com base no bot atual. '''

import random

def executar_turno_bot(bot, jogador):
    """Calcula e retorna a habilidade escolhida pelo bot com base na sua dificuldade."""
    # 1. Busca as opções (chama a função do código 1 que estará no mesmo arquivo)
    opcoes = obter_habilidades_disponiveis()
    
    # 2. Define o comportamento baseado na dificuldade do Bot atual (Padrão: FÁCIL)
    dificuldade = bot.get("dificuldade", "FÁCIL")
    
    if dificuldade == "FÁCIL" or dificuldade == "MÉDIA":
        # Sem hierarquia de força, bots fáceis e médios escolhem puramente ao acaso
        return random.choice(opcoes)
        
    elif dificuldade == "DIFÍCIL":
        # IA Inteligente: Chama a lógica avançada (que estará no mesmo arquivo)
        return logica_ia_avancada(bot, jogador, opcoes)
        
    return "habilidade_1"  # Recurso de segurança

''' AQUI EU USEI IA MAJORITÁRIAMENTE PARA PARTE DA LÓGICA. 
TAMBÉM USEI UMA BASE SINTÁTICA FORNECIDA PELA IA, PARA QUE EU PODESSE
APRENDER A CLASSIFICAR DIFICULDADE E DEPOIS REESCREVER DO MEU JEITO. '''