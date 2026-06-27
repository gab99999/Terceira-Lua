import base as b
import random

def TerceiraLua (personagem1, personagem2):
    x = random.radint(1, 5)
    if personagem1['terceira_lua'] == True:
        match x:
            case 1:
                personagem1['dano_porcentagem'] += 35
            case 2:
                personagem1['evasao'] += 4
            case 3:
                personagem1['cura_porcentagem'] += 50
            case 4:
                personagem1['precisao_bonus'] += 8
            case 5:
                personagem2["veneno"] *= 2
                personagem1['resistencia'] *= 2
                personagem1['plumas'] *= 2
    if personagem2['terceira_lua'] == True:
        match x:
            case 1:
                personagem2['dano_porcentagem'] += 35
            case 2:
                personagem2['evasao'] += 4
            case 3:
                personagem2['cura_porcentagem'] += 50
            case 4:
                personagem2['precisao_bonus'] += 8
            case 5:
                personagem1["veneno"] *= 2
                personagem2['resistencia'] *= 2
                personagem2['plumas'] *= 2