"""
Funções auxiliares utilizadas no combate.
"""

import random

# ------------------------
#          Básico
# ------------------------

def dano(min, max):
    """Retorna um dano aleatório entre min e max."""
    return random.randint(min, max)

def cura(min, max):
    """Retorna uma cura aleatória entre min e max."""
    return random.randint(min, max)


def precisao(pontos, alvo):
    """Retorna True se o teste de precisão for bem-sucedido."""
    x = random.randint(1, 100)

    print('A Lua está em: ', x)

    if alvo['cego'] == True:
        pontos = pontos//2

    if x <= pontos:
        return True
    else:
        return False


# ------------------------
#   Aumento e Diminuição
# ------------------------

def aumento_dano(porcentagem, danobase):
    """Aplica aumento percentual ao dano."""
    return danobase * (1 + porcentagem)


def aumento_cura(porcentagem, curabase):
    """Aplica aumento percentual à cura."""
    return curabase * (1 + porcentagem)


def aumento_dano_pontual(pontos, danobase):
    """Adiciona pontos fixos ao dano."""
    return pontos + danobase


def aumento_cura_pontual(pontos, curabase):
    """Adiciona pontos fixos à cura."""
    return pontos + curabase


def aumento_precisao(pontos, precisaobase):
    """Adiciona pontos fixos à precisão."""
    return pontos + precisaobase


def aumento_evasao(pontos, evasaobase):
    """Adiciona pontos fixos à evasão."""
    return pontos + evasaobase


# ------------------------
#         Extras
# ------------------------

def parar_turno(alvo, usuario):
    """Impede o alvo de agir caso o teste de precisão tenha sucesso."""
    
    if aumento_precisao(alvo['precisao_bonus'], precisao(25-alvo['evasao'], usuario)):
            alvo['pode_agir'] = False


