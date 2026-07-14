# =========================================================================================================
#                                     ESTRUTURANDO A IA DOS BOTS
# =========================================================================================================
''' Vou estruturar a IA em três níveis de de comportamento. '''

# ==============================================
#      1- ENTENDENDO AS OPÇÕES DO BOT
# ==============================================

def obter_habilidades_disponiveis():
    """Como não existem mais cooldowns, as três habilidades estão sempre prontas."""
    return ["habilidade_1", "habilidade_2", "habilidade_3"]