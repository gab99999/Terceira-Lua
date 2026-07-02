# =========================================================================================================
#                                     ESTRUTURANDO A IA DOS BOTS
# =========================================================================================================
''' Vou estruturar a IA em três níveis de de comportamento. '''

# ==============================================
#      1- ENTENDENDO AS OPÇÕES DO BOT
# ==============================================
'''A IA tem que saber o que ela pode fazer, para isso,
ela vai olhar para o próprio dicionário e verificar
quais habilidades não estão em tempo de recarga.'''

def obter_habilidades_disponiveis(self, bot):
    """Retorna uma lista com os nomes das habilidades que o bot pode usar agora."""
    disponiveis = []
    
    # Se o cooldown for 0, a habilidade básica está pronta
    if bot["cooldowns"]["habilidade1"] == 0:
        disponiveis.append("habilidade1")
        
    # Checa a temática
    if bot["cooldowns"]["habilidade2"] == 0:
        disponiveis.append("habilidade2")
        
    # Checa a ultimate (especial)
    if bot["cooldowns"]["habilidade3"] == 0:
        disponiveis.append("habilidade3")
        
    return disponiveis