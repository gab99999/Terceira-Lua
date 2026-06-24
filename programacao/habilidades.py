"""
habilidades.py

Contém todas as habilidades e passivas dos
personagens do jogo.

Cada habilidade recebe:
    usuario (dict)
    alvo (dict)
"""

import base as b
import random

# ==========================================
# AMARA
# ==========================================

def morte_lenta(usuario, alvo):
    match usuario['veneno']:
        case 0:
            pass
        case 1:
            usuario['vida'] = usuario['vida'] - b.dano(3, 7)
        case 2:
            usuario['vida'] = usuario['vida'] - b.dano(5, 10)
        case 3:
            usuario['vida'] = usuario['vida'] - b.dano(6, 12)
        case 4:
            usuario['vida'] = usuario['vida'] - b.dano(8, 16)
        case 5:
            usuario['vida'] = usuario['vida'] - b.dano(10, 20)


def reacao_magica(usuario, alvo):
    if b.aumento_precisao(alvo['precisao_bonus'], b.precisao(77-alvo['evasao'])):
        alvo['vida'] = alvo['vida'] - b.aumento_dano(alvo['dano_porcentagem'], b.dano ())
        if b.aumento_precisao(alvo['precisao_bonus'], b.precisao(25-alvo['evasao'])):
            alvo['pode_agir'] = False
    else:
        pass


def ondas_elevadas(usuario, alvo):
    pass


def cura_envenenada(usuario, alvo):
    pass


# ==========================================
# ANTONIUS
# ==========================================

def treinado_para_tudo(usuario, alvo):
    pass


def soco_tatico(usuario, alvo):
    pass


def granada_de_luz(usuario, alvo):
    pass


def tiro_certeiro(usuario, alvo):
    pass

# ==========================================
# NICOLAS
# ==========================================

def dualidade_mesclada(usuario, alvo):
    pass


def absorver_calor(usuario, alvo):
    pass


def aquecer_materia(usuario, alvo):
    pass


def fusao_magica(usuario, alvo):
    pass


# ==========================================
# PERFÍDIA
# ==========================================

def cria_lunar(usuario, alvo):
    pass


def invocacao_lunar(usuario, alvo):
    pass


def pluralidade_estelar(usuario, alvo):
    pass


def brutalizar_as_luas(usuario, alvo):
    pass

# ==========================================
# RAONI
# ==========================================

def cura_alimenta_os_fracos(usuario, alvo):
    pass


def foco_em_penas(usuario, alvo):
    pass


def especializacao_em_aves(usuario, alvo):
    pass


def inversao_curativa(usuario, alvo):
    pass


# ==========================================
# TAINÁ
# ==========================================

def dor_alimenta_os_fortes(usuario, alvo):
    pass


def dilaceracao_dupla(usuario, alvo):
    pass


def arremesso_de_lamina(usuario, alvo):
    pass


def apunhalada_pacifica(usuario, alvo):
    pass
