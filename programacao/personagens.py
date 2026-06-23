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
)

# Amara

amara = {
    "vida": 900,
    "evasao": 3,

    "passiva": morte_lenta,

    "habilidade_1": reacao_magica,
    "habilidade_2": ondas_elevadas,
    "habilidade_3": cura_envenenada
}


# Antonius

antonius = {
    "vida": 1000,
    "evasao": 5,

    "passiva": treinado_para_tudo,

    "habilidade_1": soco_tatico,
    "habilidade_2": granada_de_luz,
    "habilidade_3": tiro_certeiro
}

# Nicolas

nicolas = {
    "vida": 820,  
    "evasao": 3,  

    "passiva": dualidade_mesclada,

    "habilidade_1": absorver_calor,
    "habilidade_2": aquecer_materia,
    "habilidade_3": fusao_magica
}


# Perfídia

perfidia = {
    "vida": 780,
    "evasao": 4,

    "passiva": cria_lunar,

    "habilidade_1": invocacao_lunar,
    "habilidade_2": pluralidade_estelar,
    "habilidade_3": brutalizar_as_luas
}