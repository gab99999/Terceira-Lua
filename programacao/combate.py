# estruturas do combate



def criar_combatente(personagem):
    # cria a cópia temporária de um personagem usada em uma partida.

    combatente = personagem.copy()

    combatente["vida_maxima"] = combatente["vida"]
    combatente["pode_agir"] = True
    combatente["veneno"] = 0
    combatente["cego"] = False
    combatente["resistencia"] = 0
    combatente["plumas"] = 0
    combatente["frio"] = False
    combatente["quente"] = False
    combatente["terceira_lua"] = False
    combatente["passiva_terceira_lua_aplicada"] = False
    combatente["precisao_bonus"] = 0
    combatente["evasao_bonus"] = 0
    combatente["dano_porcentagem"] = 0
    combatente["cura_porcentagem"] = 0
    combatente["dano_pontos"] = 0
    combatente["cura_pontos"] = 0
    combatente["bonus_60_vida"] = False
    combatente["bonus_30_vida"] = False

    return combatente
