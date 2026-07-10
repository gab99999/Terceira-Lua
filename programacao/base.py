"""
Funcoes auxiliares utilizadas no combate.
"""

import random

# ------------------------
#          Basico
# ------------------------

def dano(minimo, maximo):
    """Retorna um dano aleatorio."""
    return random.randint(minimo, maximo)


def cura(minimo, maximo):
    """Retorna uma cura aleatoria."""
    return random.randint(minimo, maximo)


def precisao(chance, usuario):
    """
    Realiza um teste de precisao.
    Leva em consideracao a cegueira e o bonus de precisao.
    """

    chance += usuario.get("precisao_bonus", 0)

    if usuario.get("cego", False):
        chance //= 2

    chance = max(0, min(100, chance))

    lua = random.randint(1, 100)
    print(f"A Lua esta em: {lua}")

    return lua <= chance


# ------------------------
#   Aumento e diminuicao
# ------------------------

def aumento_dano(porcentagem, dano_base):
    """Aplica aumento percentual ao dano."""
    return dano_base * (1 + porcentagem)


def aumento_cura(porcentagem, cura_base):
    """Aplica aumento percentual a cura."""
    return cura_base * (1 + porcentagem)


def aumento_dano_pontual(pontos, dano_base):
    """Aplica aumento fixo ao dano."""
    return dano_base + pontos


def aumento_cura_pontual(pontos, cura_base):
    """Aplica aumento fixo a cura."""
    return cura_base + pontos


def aumento_precisao(pontos, precisao_base):
    """Retorna uma precisao com bonus."""
    return precisao_base + pontos


def aumento_evasao(pontos, evasao_base):
    """Retorna uma evasao com bonus."""
    return evasao_base + pontos


# ------------------------
#         Extras
# ------------------------

def parar_turno(alvo, usuario, chance):
    """
    Impede o alvo de agir caso o teste de precisao seja bem-sucedido.
    """

    if precisao(chance - alvo.get("evasao", 0), usuario):
        alvo["pode_agir"] = False


def limitar_vida(personagem):
    """Impede que a vida fique abaixo de 0 ou acima do maximo."""

    vida_maxima = personagem.get("vida_maxima", personagem["vida"])

    if personagem["vida"] > vida_maxima:
        personagem["vida"] = vida_maxima

    if personagem["vida"] < 0:
        personagem["vida"] = 0
