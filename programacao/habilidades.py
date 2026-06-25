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
    antonius_dano(usuario)

# VAI PRECISAR DE BALANCEAMENTO

def reacao_magica(usuario, alvo):
    if b.aumento_precisao(alvo['precisao_bonus'], b.precisao(77-alvo['evasao'], usuario)):
        alvo['vida'] = alvo['vida'] - b.aumento_dano(alvo['dano_porcentagem'], b.dano (50, 115))
        alvo['veneno'] += 2
        antonius_dano(alvo)
        b.parar_turno(alvo,usuario)
    else:
        if alvo['veneno'] > 0:
            alvo['veneno'] -= 1
        

def ondas_elevadas(usuario, alvo):
    if b.aumento_precisao(alvo['precisao_bonus'], b.precisao(86-alvo['evasao'], usuario)):
        alvo['vida'] = alvo['vida'] - b.aumento_dano(alvo['dano_porcentagem'], b.dano (60, 100))
        alvo['veneno'] += 1
        antonius_dano(alvo)
    else:
        if alvo['veneno'] > 0:
            alvo['veneno'] -= 1



def cura_envenenada(usuario, alvo):
    if b.aumento_precisao(alvo['precisao_bonus'], b.precisao(86-alvo['evasao'], usuario)):
        alvo['vida'] = alvo['vida'] - b.aumento_dano(alvo['dano_porcentagem'], b.dano (80, 140))
        antonius_dano(alvo)

        match alvo['veneno']:
            case 0:
                pass
            case 1:
                usuario['vida'] = usuario['vida'] + b.aumento_cura(usuario['cura_porcentagem'], b.cura(7, 7)*2)
            case 2:
                usuario['vida'] = usuario['vida'] + b.aumento_cura(usuario['cura_porcentagem'], b.cura(10, 10)*2)
            case 3:
                usuario['vida'] = usuario['vida'] + b.aumento_cura(usuario['cura_porcentagem'], b.cura(12, 12)*2)
            case 4:
                usuario['vida'] = usuario['vida'] + b.aumento_cura(usuario['cura_porcentagem'], b.cura(16, 16)*2)
            case _:
                usuario['vida'] = usuario['vida'] + b.aumento_cura(usuario['cura_porcentagem'], b.cura(20, 20)*2)
        if usuario['vida']>usuario['vida_maxima']:
            usuario['vida'] = usuario['vida_maxima']
                
        alvo['veneno'] = 0

        alvo['veneno'] += 2
    else:
        if alvo['veneno'] > 0:
            alvo['veneno'] -= 1


# ==========================================
# ANTONIUS
# ==========================================

def antonius_dano(alvo):
    if alvo['nome'] == 'Antonius':
        alvo['resistencia'] += 1


def treinado_para_tudo(usuario, alvo):
    if usuario['nome'] == 'Antonius' and usuario['resistencia'] >= 1: 
        x = random.radint(1, 3)
        match x:
            case 1:
                usuario['evasao'] += 1
                print ('Evasão Aumentada!')
            case 2:
                usuario['precisao_bonus'] += 1
            case 3:
                usuario['vida'] += b.aumento_cura(usuario['cura_porcentagem'], b.cura(0, 30))
                if usuario['vida']>usuario['vida_maxima']:
                    usuario['vida'] = usuario['vida_maxima']
        


def soco_tatico(usuario, alvo):
    if b.aumento_precisao(alvo['precisao_bonus'], b.precisao(75-alvo['evasao'], usuario)):
        alvo['vida'] = alvo['vida'] - b.aumento_dano(alvo['dano_porcentagem'], b.dano (55, 115))
        antonius_dano(alvo)
    

def granada_de_luz(usuario, alvo):
    if b.aumento_precisao(alvo['precisao_bonus'], b.precisao(75-alvo['evasao']), usuario):
        alvo['vida'] = alvo['vida'] - b.aumento_dano(alvo['dano_porcentagem'], b.dano (45, 100))
        antonius_dano(alvo)
        if b.aumento_precisao(alvo['precisao_bonus'], b.precisao(25-alvo['evasao'])):
            alvo["cego"] = True


def tiro_certeiro(usuario, alvo):
    if b.aumento_precisao(alvo['precisao_bonus'], b.precisao(55-alvo['evasao']), usuario):
        alvo['vida'] = alvo['vida'] - b.aumento_dano(alvo['dano_porcentagem'], b.dano (100, 240))
        antonius_dano(alvo)

        b.parar_turno(alvo,usuario)  


# ==========================================
# NICOLAS
# ==========================================

def dualidade_mesclada(usuario, alvo):
    if usuario['frio'] and usuario['quente']:
        alvo['vida'] -= b.aumento_dano(alvo['dano_porcentagem'], b.dano (0, 120))
        antonius_dano(alvo)
        usuario['frio'] = False
        usuario['quente'] = False


def absorver_calor(usuario, alvo):
    if b.aumento_precisao(alvo['precisao_bonus'], b.precisao(75-alvo['evasao']), usuario):
        alvo['vida'] = alvo['vida'] - b.aumento_dano(alvo['dano_porcentagem'], b.dano (70, 110))
        antonius_dano(alvo)
        usuario['frio'] = True
        dualidade_mesclada(usuario, alvo)


def aquecer_materia(usuario, alvo):
    if b.aumento_precisao(alvo['precisao_bonus'], b.precisao(75-alvo['evasao']), usuario):
        alvo['vida'] = alvo['vida'] - b.aumento_dano(alvo['dano_porcentagem'], b.dano (60, 120))
        antonius_dano(alvo)
        usuario['quente'] = True
        dualidade_mesclada(usuario, alvo)


def fusao_magica(usuario, alvo):
    if b.aumento_precisao(alvo['precisao_bonus'], b.precisao(60-alvo['evasao']), usuario):
        alvo['vida'] = alvo['vida'] - b.aumento_dano(alvo['dano_porcentagem'], b.dano (100, 200))
        antonius_dano(alvo)
        b.parar_turno(alvo, usuario)



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

def cura_alimenta_os_fracos(usuario, dano):
    b.aumento_dano_pontual(usuario['plumas'], dano)


def foco_em_penas(usuario, alvo):
    if b.aumento_precisao(alvo['precisao_bonus'], b.precisao(85-alvo['evasao']), usuario):
        alvo['vida'] = alvo['vida'] - b.aumento_dano(alvo['dano_porcentagem'], cura_alimenta_os_fracos(usuario, b.dano (50, 85)))
        antonius_dano(alvo)
        usuario['plumas'] += 4
        usuario['vida'] += b.aumento_cura(usuario['cura_porcentagem'], b.cura(20, 40))
        if usuario['vida']>usuario['vida_maxima']:
            usuario['vida'] = usuario['vida_maxima']
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
