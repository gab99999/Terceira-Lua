from personagens import personagens as skill
import random

# ------------------------
#          Funções
# ------------------------

def criar_combatente(personagem):
    combatente = personagem.copy()

    combatente["vida_maxima"] = combatente["vida"]

    combatente["pode_agir"] = True

    combatente["veneno"] = 0
    combatente["cego"] = 0

    combatente["precisao_bonus"] = 0
    combatente["evasao_bonus"] = 0

    combatente["dano_bonus"] = 0
    combatente["cura_bonus"] = 0

    return combatente

# ------------------------
#        Variáveis
# ------------------------

escolha1 = 'Amara'
escolha2 = 'Perfídia'

personagem1 = criar_combatente(skill[escolha1])
personagem2 = criar_combatente(skill[escolha2])

qualturno = random.choice([True, False])

# ------------------------
#         Combate
# ------------------------

while personagem1['vida'] > 0 and personagem2['vida'] > 0:
    if qualturno:
        if personagem1['pode_agir']:
            print(personagem1)
    else:
        if personagem2['pode_agir']:
            print(personagem2)
    if qualturno:
        personagem1['pode_agir'] = True
    else:
        personagem2['pode_agir'] = True
    qualturno = not qualturno
    qntturno += 1


        

