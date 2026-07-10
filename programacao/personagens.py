"""
personagens.py

Contém todos os personagens jogáveis do projeto
Terceira Lua.

Cada personagem é armazenado em um dicionário
com seus atributos básicos, passiva e habilidades.
"""

import base as b 
import random

from habilidades import (
    morte_lenta,
    reacao_magica,
    ondas_elevadas,
    cura_envenenada,

    treinado_para_tudo,
    soco_tatico,
    granada_de_luz,
    tiro_certeiro,

    dualidade_mesclada,
    absorver_calor,
    aquecer_materia,
    fusao_magica,

    cria_lunar,
    invocacao_lunar,
    pluralidade_estelar,
    brutalizar_as_luas,

    cura_alimenta_os_fracos,
    foco_em_penas,
    especializacao_em_aves,
    inversao_curativa,

    dor_alimenta_os_fortes,
    dilaceracao_dupla,
    arremesso_de_lamina,
    apunhalada_pacifica
)


# Amara

amara = {
    'nome': 'Amara',
    "vida": 900,
    "evasao": 3,

    "passiva": morte_lenta,

    "habilidade_1": reacao_magica,
    "habilidade_2": ondas_elevadas,
    "habilidade_3": cura_envenenada
}


# Antonius

antonius = {
    'nome': 'Antonius',
    "vida": 1000,
    "evasao": 5,

    "passiva": treinado_para_tudo,

    "habilidade_1": soco_tatico,
    "habilidade_2": granada_de_luz,
    "habilidade_3": tiro_certeiro
}

# Nicholas

nicholas = {
    'nome': 'Nicholas',
    "vida": 820,  
    "evasao": 0,  

    "passiva": dualidade_mesclada,

    "habilidade_1": absorver_calor,
    "habilidade_2": aquecer_materia,
    "habilidade_3": fusao_magica
}


# Perfídia

perfidia = {
    'nome': 'Perfídia',
    "vida": 780,
    "evasao": 5,

    "passiva": cria_lunar,

    "habilidade_1": invocacao_lunar,
    "habilidade_2": pluralidade_estelar,
    "habilidade_3": brutalizar_as_luas
}


# Raoni

raoni = {
    'nome': 'Raoni',
    "vida": 640,
    "evasao": 2,

    "passiva": cura_alimenta_os_fracos,

    "habilidade_1": foco_em_penas,
    "habilidade_2": especializacao_em_aves,
    "habilidade_3": inversao_curativa
}


# Tainá

taina = {
    'nome': 'Tainá',
    "vida": 700,
    "evasao": 14,

    "passiva": dor_alimenta_os_fortes,

    "habilidade_1": dilaceracao_dupla,
    "habilidade_2": arremesso_de_lamina,
    "habilidade_3": apunhalada_pacifica
}

personagens = {
    "Amara": amara,
    "Antonius": antonius,
    "Nicholas": nicholas,
    "Perfídia": perfidia,
    "Raoni": raoni,
    "Tainá": taina
}
