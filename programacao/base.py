"""
Funções auxiliares utilizadas no combate.
"""

import random

# ------------------------
#          Básico
# ------------------------

def dano(minimo, maximo):
    """Retorna um dano aleatório."""
    return random.randint(minimo, maximo)


def cura(minimo, maximo):
    """Retorna uma cura aleatória."""
    return random.randint(minimo, maximo)


def precisao(chance, usuario):
    """
    Realiza um teste de precisão.
    Leva em consideração a cegueira e o bônus de precisão.
    """

    # Aplica bônus de precisão
    chance += usuario["precisao_bonus"]

    # Se estiver cego, a precisão é reduzida pela metade
    if usuario["cego"]:
        chance //= 2

    # Limita a chance entre 0 e 100
    chance = max(0, min(100, chance))

    lua = random.randint(1, 100)
    print(f"A Lua está em: {lua}")

    return lua <= chance


# ------------------------
#   Aumento e Diminuição
# ------------------------

def aumento_dano(porcentagem, dano_base):
    """Aplica aumento percentual ao dano."""
    return dano_base * (1 + porcentagem)


def aumento_cura(porcentagem, cura_base):
    """Aplica aumento percentual à cura."""
    return cura_base * (1 + porcentagem)


def aumento_dano_pontual(pontos, dano_base):
    """Aplica aumento fixo ao dano."""
    return dano_base + pontos


def aumento_cura_pontual(pontos, cura_base):
    """Aplica aumento fixo à cura."""
    return cura_base + pontos


def aumento_precisao(pontos, precisao_base):
    """Retorna uma precisão com bônus."""
    return precisao_base + pontos


def aumento_evasao(pontos, evasao_base):
    """Retorna uma evasão com bônus."""
    return evasao_base + pontos


# ------------------------
#         Extras
# ------------------------

def parar_turno(alvo, usuario, chance):
    """
    Impede o alvo de agir caso o teste de precisão seja bem-sucedido.
    """

    if precisao(chance - alvo["evasao"], usuario):
        alvo["pode_agir"] = False

def limitar_vida(personagem):
    """Impede que a vida ultrapasse o máximo."""

    if personagem["vida"] > personagem["vida_maxima"]:
        personagem["vida"] = personagem["vida_maxima"]

    if personagem["vida"] < 0:
        personagem["vida"] = 0