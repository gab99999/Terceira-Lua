import random

# ------------------------
#          Básico
# ------------------------
def dano (min, max):
    return random.randint (min, max)

def precisao(pontos):
    x = random.randint (1, 100)
    if x <= pontos:
        return True
    else:
        return False
    
# ------------------------
#   Aumento e Diminuição
# ------------------------
    
def aumento_dano (porcentagem, danobase):
    return danobase * (1+porcentagem)

def aumento_cura (porcentagem, curabase):
    return curabase * (1+porcentagem)

def aumento_dano_pontual (pontos, danobase):
    return pontos + danobase

def aumento_cura_pontual (pontos, curabase):
    return pontos + curabase

def aumento_precisao (pontos, precisaobase):
    return pontos + precisaobase

def aumento_evasao (pontos, evasaobase):
    return pontos + evasaobase

# ------------------------
#         Extras
# ------------------------

def parar_turno(pontos):
    return (not precisao(pontos))






