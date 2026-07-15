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
    "habilidade_3": cura_envenenada,

    "historia": "Uma química renomada, Amara proporciona a mistura da ciência e magia. Ela modifica seus estudos químicos para criar magia. É secretamente apaixonada por Tainá. Faz piadas sem graça sobre químicos e magia. Time dos Lunaristas.",
    "tom": "inteligentemente irritante"
}


# Antonius

antonius = {
    'nome': 'Antonius',
    "vida": 1000,
    "evasao": 5,

    "passiva": treinado_para_tudo,

    "habilidade_1": soco_tatico,
    "habilidade_2": granada_de_luz,
    "habilidade_3": tiro_certeiro,

    "historia": "Ex-militar, Antonius tem o treinamento especializado foi treinado para todas as situações de combate, até a chegada da Segunda Lua mudar isso. Ele sente muito rancor da magia e seus usuários. Time dos praguistas",
    "tom": "disciplinado"
}

# Nicholas

nicholas = {
    'nome': 'Nicholas',
    "vida": 820,  
    "evasao": 0,  

    "passiva": dualidade_mesclada,

    "habilidade_1": absorver_calor,
    "habilidade_2": aquecer_materia,
    "habilidade_3": fusao_magica,

    "historia": "Estudou com Perfídia, mas agora pensa que a magia é uma droga viciante se usada de maneira errada. Utiliza magia mesmo sendo contra ela. Time dos praguistas",
    "tom": "arrogante"
}


# Perfídia

perfidia = {
    'nome': 'Perfídia',
    "vida": 780,
    "evasao": 5,

    "passiva": cria_lunar,

    "habilidade_1": invocacao_lunar,
    "habilidade_2": pluralidade_estelar,
    "habilidade_3": brutalizar_as_luas,

    "historia": "Uma das mais famosas ativistas Lunaristas, Perfídia usa magia pura da luz das Luas. Ela acredita fielmente que é filha das luas. Time dos lunaristas",
    "tom": "irritantemente simpática"
}


# Raoni

raoni = {
    'nome': 'Raoni',
    "vida": 640,
    "evasao": 2,

    "passiva": cura_alimenta_os_fracos,

    "habilidade_1": foco_em_penas,
    "habilidade_2": especializacao_em_aves,
    "habilidade_3": inversao_curativa,

    "historia": "Irmão de Tainá, ele afirma que a magia reviveu sua cultura e vai curar o planeta. Utiliza de pássaros para suas magias. Sua mãe tentou conduzir um ritual com magia e morreu. Time dos lunaristas",
    "tom": "gentil mas raivoso ao mesmo tempo"
}


# Tainá

taina = {
    'nome': 'Tainá',
    "vida": 700,
    "evasao": 14,

    "passiva": dor_alimenta_os_fortes,

    "habilidade_1": dilaceracao_dupla,
    "habilidade_2": arremesso_de_lamina,
    "habilidade_3": apunhalada_pacifica,

    "historia": "Irmã de Raoni, ela afirma que a magia assassinou a sua mãe. Utiliza de adagas para eliminar seus inimigos. Sua mãe tentou conduzir um ritual com magia e morreu, por isso sente raiva de seu irmão Raoni que usa magia. Time dos lunaristas",
    "tom": "séria, mas sempre com ar de estar sentindo tédio"
}

personagens = {
    "Amara": amara,
    "Antonius": antonius,
    "Nicholas": nicholas,
    "Perfidia": perfidia,
    "Raoni": raoni,
    "Taina": taina
}
