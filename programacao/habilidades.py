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

# Aplica o dano do veneno mágico.
def morte_lenta(usuario, alvo):
    match usuario['veneno']:
        case 0:
            return
        case 1:
            usuario['vida'] -= b.dano(3, 7)
        case 2:
            usuario['vida'] -= b.dano(5, 10)
        case 3:
            usuario['vida'] -= b.dano(6, 12)
        case 4:
            usuario['vida'] -= b.dano(8, 16)
        case _:
            usuario['vida'] -= b.dano(10, 20)

    antonius_dano(usuario)


# Habilidade 1
def reacao_magica(usuario, alvo):
    if b.precisao(77 - alvo['evasao'], usuario):
        dano = b.dano(50, 115)
        dano = b.aumento_dano(usuario['dano_porcentagem'], dano)
        alvo['vida'] -= dano
        alvo['veneno'] += 2
        antonius_dano(alvo)
        if b.precisao(25 - alvo['evasao'], usuario):
            alvo['evasao'] -= 1

    elif alvo['veneno'] > 0:
        alvo['veneno'] -= 1


# Habilidade 2
def ondas_elevadas(usuario, alvo):
    if b.precisao(86 - alvo['evasao'], usuario):
        dano = b.dano(60, 100)
        dano = b.aumento_dano(usuario['dano_porcentagem'], dano)
        alvo['vida'] -= dano
        alvo['veneno'] += 1

        antonius_dano(alvo)

    elif alvo['veneno'] > 0:
        alvo['veneno'] -= 1


# Habilidade 3
def cura_envenenada(usuario, alvo):
    if b.precisao(60 - alvo['evasao'], usuario):
        dano = b.dano(80, 140)
        dano = b.aumento_dano(usuario['dano_porcentagem'], dano)
        alvo['vida'] -= dano
        antonius_dano(alvo)
        match alvo['veneno']:
            case 0:
                cura = 0
            case 1:
                cura = b.cura(7, 7) * 2
            case 2:
                cura = b.cura(10, 10) * 2
            case 3:
                cura = b.cura(12, 12) * 2
            case 4:
                cura = b.cura(16, 16) * 2
            case _:
                cura = b.cura(20, 20) * 2
        cura = b.aumento_cura(usuario['cura_porcentagem'], cura)

        usuario['vida'] += cura
        b.limitar_vida(usuario)

        alvo['veneno'] = 2
    elif alvo['veneno'] > 0:
        alvo['veneno'] -= 1

# ==========================================
# ANTONIUS
# ==========================================

# Sempre que Antonius sofre dano, ganha resistência.
def antonius_dano(alvo):
    if alvo['nome'] == 'Antonius':
        alvo['resistencia'] += 1


# Gasta automaticamente um ponto de resistência.
def treinado_para_tudo(usuario, alvo):
    if usuario['nome'] == 'Antonius' and usuario['resistencia'] > 0:
        # Consome um ponto de resistência
        usuario['resistencia'] -= 1
        x = random.randint(1, 3)

        match x:

            case 1:
                usuario['evasao'] += 1
                print('Evasão aumentada!')
            case 2:
                usuario['precisao_bonus'] += 1
                print('Precisão aumentada!')

            case 3:
                cura = b.cura(0, 30)
                cura = b.aumento_cura(usuario['cura_porcentagem'], cura)
                usuario['vida'] += cura
                b.limitar_vida(usuario)

                print('Antonius recuperou vida!')

# Habilidade 1
def soco_tatico(usuario, alvo):
    if b.precisao(75 - alvo['evasao'], usuario):
        dano = b.dano(55, 115)
        dano = b.aumento_dano(usuario['dano_porcentagem'], dano)
        alvo['vida'] -= dano
        antonius_dano(alvo)
    
# Habilidade 2
def granada_de_luz(usuario, alvo):
    if b.precisao(75 - alvo['evasao'], usuario):
        dano = b.dano(45, 100)
        dano = b.aumento_dano(usuario['dano_porcentagem'], dano)
        alvo['vida'] -= dano
        antonius_dano(alvo)

        if b.precisao(25 - alvo['evasao'], usuario):
            alvo['cego'] = True

# Habilidade 3
def tiro_certeiro(usuario, alvo):
    if b.precisao(55 - alvo['evasao'], usuario):
        dano = b.dano(100, 240)
        dano = b.aumento_dano(usuario['dano_porcentagem'], dano)
        alvo['vida'] -= dano
        antonius_dano(alvo)

        b.parar_turno(alvo, usuario, 10)


# ==========================================
# NICOLAS
# ==========================================

# Ativa o choque térmico ao combinar frio e calor.
def dualidade_mesclada(usuario, alvo):

    if usuario['frio'] and usuario['quente']:
        dano = b.dano(0, 120)
        dano = b.aumento_dano(usuario['dano_porcentagem'], dano)
        alvo['vida'] -= dano
        antonius_dano(alvo)

        usuario['frio'] = False
        usuario['quente'] = False


# Habilidade 1
def absorver_calor(usuario, alvo):

    if b.precisao(75 - alvo['evasao'], usuario):
        dano = b.dano(75, 110)
        dano = b.aumento_dano(usuario['dano_porcentagem'], dano)
        alvo['vida'] -= dano
        antonius_dano(alvo)
        usuario['frio'] = True
        dualidade_mesclada(usuario, alvo)


# Habilidade 2
def aquecer_materia(usuario, alvo):
    if b.precisao(75 - alvo['evasao'], usuario):
        dano = b.dano(60, 140)
        dano = b.aumento_dano(usuario['dano_porcentagem'], dano)
        alvo['vida'] -= dano
        antonius_dano(alvo)

        usuario['quente'] = True
        dualidade_mesclada(usuario, alvo)


# Habilidade 3
def fusao_magica(usuario, alvo):

    if b.precisao(60 - alvo['evasao'], usuario):
        dano = b.dano(100, 200)
        dano = b.aumento_dano(usuario['dano_porcentagem'], dano)
        alvo['vida'] -= dano
        antonius_dano(alvo)

        b.parar_turno(alvo, usuario, 10)


# Buffs exclusivos após a Terceira Lua.
# ==========================================
# PERFÍDIA
# ==========================================

# Passiva
def cria_lunar(usuario, alvo):

    if usuario['terceira_lua']:
        usuario['dano_porcentagem'] += 0.05
        usuario['evasao'] += 1
        usuario['cura_porcentagem'] += 0.10
        usuario['precisao_bonus'] += 2

        alvo['terceira_lua'] = False
        usuario['terceira_lua'] = False

# Habilidade 1
def invocacao_lunar(usuario, alvo):

    if usuario['terceira_lua']:
        precisao = 80
        dano = b.dano(90, 120)

    else:
        precisao = 90
        dano = b.dano(55, 75)

    if b.precisao(precisao - alvo['evasao'], usuario):

        dano = b.aumento_dano(usuario['dano_porcentagem'], dano)
        alvo['vida'] -= dano

        antonius_dano(alvo)
        b.limitar_vida(alvo)
        if usuario['terceira_lua']:

            cura = b.cura(45, 60)
            cura = b.aumento_cura(usuario['cura_porcentagem'], cura)

            usuario['vida'] += cura

            b.limitar_vida(usuario)
        else:

            # diminuir em 1 turno a chegada da Terceira Lua
            pass

# Habilidade 2
def pluralidade_estelar(usuario, alvo):

    if usuario['terceira_lua']:
        precisao = 75
        dano = b.dano(110, 140)
        cura = b.cura(40, 55)

    else:
        precisao = 75
        dano = b.dano(55, 85)
        cura = b.cura(30, 50)

    if b.precisao(precisao - alvo['evasao'], usuario):
        dano = b.aumento_dano(usuario['dano_porcentagem'], dano)
        alvo['vida'] -= dano
        antonius_dano(alvo)
        b.limitar_vida(alvo)
        cura = b.aumento_cura(usuario['cura_porcentagem'], cura)
        usuario['vida'] += cura
        b.limitar_vida(usuario)
    

# Habilidade 3
def brutalizar_as_luas(usuario, alvo):

    if usuario['terceira_lua']:
        precisao = 85
        dano = b.dano(85, 110)
    else:
        precisao = 85
        dano = b.dano(30, 60)

    if b.precisao(precisao - alvo['evasao'], usuario):
        dano = b.aumento_dano(usuario['dano_porcentagem'], dano)
        alvo['vida'] -= dano
        antonius_dano(alvo)
        b.limitar_vida(alvo)
        if usuario['terceira_lua']:

            if random.randint(1, 100) <= 25:
                alvo['pode_agir'] = False
        else:

            # diminuir de 1 a 2 turnos a chegada da Terceira Lua
            pass

# ==========================================
# RAONI
# ==========================================

# Aumenta o dano conforme as plumas acumuladas.
def cura_alimenta_os_fracos(usuario, dano):
    if not isinstance(dano, (int, float)):
        return 0
    return b.aumento_dano_pontual(usuario['plumas'], dano)

# Habilidade 1
def foco_em_penas(usuario, alvo):
    if b.precisao(85 - alvo['evasao'], usuario):
        dano = b.dano(50, 85)
        dano = cura_alimenta_os_fracos(usuario, dano)
        dano = b.aumento_dano(usuario['dano_porcentagem'], dano)
        alvo['vida'] -= dano
        antonius_dano(alvo)
        b.limitar_vida(alvo)
        usuario['plumas'] += 4
        cura = b.cura(20, 40)
        cura = b.aumento_cura(usuario['cura_porcentagem'], cura)
        usuario['vida'] += cura
        b.limitar_vida(usuario)

# Habilidade 2
def especializacao_em_aves(usuario, alvo):
    if b.precisao(85 - alvo['evasao'], usuario):
        dano = b.dano(75, 95)
        dano = cura_alimenta_os_fracos(usuario, dano)
        dano = b.aumento_dano(usuario['dano_porcentagem'], dano)
        alvo['vida'] -= dano
        antonius_dano(alvo)
        b.limitar_vida(alvo)
        usuario['plumas'] += 3
        cura = b.cura(35, 50)
        cura = b.aumento_cura(usuario['cura_porcentagem'], cura)
        usuario['vida'] += cura
        b.limitar_vida(usuario)

# Habilidade 3
def inversao_curativa(usuario, alvo):
    if b.precisao(85 - alvo['evasao'], usuario):
        dano = b.dano(50, 85)
        dano = cura_alimenta_os_fracos(usuario, dano)
        dano = b.aumento_dano(usuario['dano_porcentagem'], dano)
        alvo['vida'] -= dano
        antonius_dano(alvo)
        b.limitar_vida(alvo)
        alvo['cura_porcentagem'] -= 0.15


# ==========================================
# TAINÁ
# ==========================================

# Aumenta o dano conforme a vida diminui.
def dor_alimenta_os_fortes(usuario, alvo):
    if usuario['vida'] < usuario['vida_maxima'] * 0.6 and not usuario.get('bonus_60_vida'):
        usuario['dano_porcentagem'] += 0.40
        usuario['bonus_60_vida'] = True
    if usuario['vida'] < usuario['vida_maxima'] * 0.3 and not usuario.get('bonus_30_vida'):
        usuario['dano_porcentagem'] += 0.40
        usuario['bonus_30_vida'] = True

# Habilidade 1
def dilaceracao_dupla(usuario, alvo):
    if b.precisao(78 - alvo['evasao'], usuario):
        dano = b.dano(70, 120)
        dano = b.aumento_dano(usuario['dano_porcentagem'], dano)
        alvo['vida'] -= dano
        antonius_dano(alvo)
        b.limitar_vida(alvo)
        usuario['vida'] -= b.dano(30, 50)
        b.limitar_vida(usuario)
        alvo['precisao_bonus'] -= 1

# Habilidade 2
def arremesso_de_lamina(usuario, alvo):
    if b.precisao(78 - alvo['evasao'], usuario):
        dano = b.dano(70, 150)
        dano = b.aumento_dano(usuario['dano_porcentagem'], dano)
        alvo['vida'] -= dano
        antonius_dano(alvo)
        b.limitar_vida(alvo)
        usuario['vida'] -= b.dano(35, 75)
        b.limitar_vida(usuario)
        if random.randint(1, 100) <= 50:
            usuario['evasao'] += 1

# Habilidade 3
def apunhalada_pacifica(usuario, alvo):
    if b.precisao(50 - alvo['evasao'], usuario):
        dano = b.dano(125, 250)
        dano = b.aumento_dano(usuario['dano_porcentagem'], dano)
        alvo['vida'] -= dano
        antonius_dano(alvo)
        b.limitar_vida(alvo)

