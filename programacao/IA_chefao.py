# ========================================
#       CRIANDO IA AVANÇADA (CHEFE)
# ========================================
''' Para os bots mais difíceis ou chefes das fases avançadas, a IA precisa
analisar o contexto da batalha. Um exemplo é se ele estiver morrendo e tiver
uma habilidade se cura ou escudo, ele deve priorizar isso em vez de apenas atacar. '''

import random

def logica_ia_avancada(bot, jogador, opcoes):
    """Lógica onde o chefe analisa o contexto para tomar a melhor decisão."""
    # Regra de Sobrevivência: Verifica se a vida do bot está abaixo ou igual a 30%
    vida_critica = (bot["vida_atual"] / bot["vida_maxima"]) <= 0.30
    
    if vida_critica:
        # Se estiver morrendo, ele ignora o erro e foca na habilidade_2 (defesa/cura)
        return "habilidade_2"
        
    # Se a vida estiver segura, ele joga de forma imprevisível usando qualquer uma das três
    return random.choice(opcoes)