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
        case _:
            usuario['vida'] = usuario['vida'] - b.dano(10, 20)

# VAI PRECISAR DE BALANCEAMENTO

def reacao_magica(usuario, alvo):
    if b.aumento_precisao(alvo['precisao_bonus'], b.precisao(77-alvo['evasao'])):
        alvo['vida'] = alvo['vida'] - b.aumento_dano(alvo['dano_porcentagem'], b.dano (50, 115))
        alvo['veneno'] += 2
        if b.aumento_precisao(alvo['precisao_bonus'], b.precisao(25-alvo['evasao'])):
            alvo['pode_agir'] = False
        else:
            pass
    else:
        if alvo['veneno'] > 0:
            alvo['veneno'] -= 1
        

def ondas_elevadas(usuario, alvo):
    if b.aumento_precisao(alvo['precisao_bonus'], b.precisao(86-alvo['evasao'])):
        alvo['vida'] = alvo['vida'] - b.aumento_dano(alvo['dano_porcentagem'], b.dano (60, 100))
        alvo['veneno'] += 1
    else:
        if alvo['veneno'] > 0:
            alvo['veneno'] -= 1



def cura_envenenada(usuario, alvo):
    if b.aumento_precisao(alvo['precisao_bonus'], b.precisao(86-alvo['evasao'])):
        alvo['vida'] = alvo['vida'] - b.aumento_dano(alvo['dano_porcentagem'], b.dano (80, 140))

        match alvo['veneno']:
            case 0:
                pass
            case 1:
                usuario['vida'] = usuario['vida'] + b.aumento_cura(usuario['cura_porcentagem'], b.cura(7*2))
            case 2:
                usuario['vida'] = usuario['vida'] + b.aumento_cura(usuario['cura_porcentagem'], b.cura(10*2))
            case 3:
                usuario['vida'] = usuario['vida'] + b.aumento_cura(usuario['cura_porcentagem'], b.cura(12*2))
            case 4:
                usuario['vida'] = usuario['vida'] + b.aumento_cura(usuario['cura_porcentagem'], b.cura(16*2))
            case _:
                usuario['vida'] = usuario['vida'] + b.aumento_cura(usuario['cura_porcentagem'], b.cura(20*2))
                
        alvo['veneno'] = 0

        alvo['veneno'] += 2
    else:
        if alvo['veneno'] > 0:
            alvo['veneno'] -= 1


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
