# ========================================
#       CRIANDO IA AVANÇADA (CHEFE)
# ========================================
''' Para os bots mais difíceis ou chefes das fases avançadas, a IA precisa
analisar o contexto da batalha. Um exemplo é se ele estiver morrendo e tiver
uma habilidade se cura ou escudo, ele deve priorizar isso em vez de apenas atacar. '''

def logica_ia_avancada(self, opcoes):
    """Lógica onde o bot analisa a situação para tomar a melhor decisão."""
    
    # Regra de Sobrevivência: Se a vida do bot estiver abaixo de 30%
    vida_critica = (self.bot["vida_atual"] / self.bot["vida_maxima"]) <= 0.30
    
    if vida_critica and "habilidade_tematica" in opcoes:
        # Supondo que a habilidade2 desse bot seja de defesa/cura
        print("💡 [IA] Bot detectou vida baixa e decidiu se defender!")
        return "habilidade2"
        
    # Regra de Ataque Máximo: Se a habilidade3 estiver pronta, use sem dó!
    if "habilidade3" in opcoes:
        print("💡 [IA] Bot viu uma oportunidade e usou o Especial!")
        return "habilidade3"
        
    # Regra de Oportunidade: Se o jogador estiver com pouca vida, finalize-o
    if self.jogador["vida_atual"] <= 20:
        # Se o bot tiver uma habilidade2 de dano alto pronta, usa ela
        if "habilidade2" in opcoes:
            return "habilidade2"
            
    # Se nenhuma regra especial se aplicar, usa o que estiver disponível
    if "habilidade2" in opcoes:
        return "habilidade2"
        
    return "habilidade1"