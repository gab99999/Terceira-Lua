import random
import base as b

# ==========================================
#       INTERACOES DISPONIVEIS
# ==========================================

def criar_interacoes():

 #   Cria as interacoes que ainda podem ser tentadas durante a batalha


    return {
        "estrela_de_cura": estrela_de_cura,
        "estrela_de_precisao": estrela_de_precisao,
        "estrela_de_dano": estrela_de_dano,
        "estrela_da_evasao": estrela_da_evasao,
        "estrela_misteriosa": estrela_misteriosa,
        "absorver_sol": absorver_sol
    }


def tentar_interacao(nome, interacoes_restantes, usuario, alvo):
  #  Cada estrela especifica e o Absorver Sol so podem ser tentados uma vez

    if nome not in interacoes_restantes:
        print("Essa interacao nao esta mais disponivel.")
        return False
    interacao = interacoes_restantes.pop(nome)
    interacao(usuario, alvo)
    return True

# ==========================================
#          CAPTURAR ESTRELA
# ==========================================

# Detalhes das Interações estão em interacoes.md

def estrela_de_cura(usuario, alvo):
    if b.precisao(45 - alvo.get('evasao', 0), usuario):
        cura = b.cura(100, 200)
        cura = b.aumento_cura(usuario['cura_porcentagem'], cura)
        usuario['vida'] += cura
        b.limitar_vida(usuario)


def estrela_de_precisao(usuario, alvo):
    if b.precisao(35 - alvo.get('evasao', 0), usuario):
        bonus = random.randint(8, 10)
        usuario['precisao_bonus'] += bonus

def estrela_de_dano(usuario, alvo):
    if b.precisao(40 - alvo.get('evasao', 0), usuario):
        usuario['dano_porcentagem'] += 0.25

def estrela_da_evasao(usuario, alvo):
    if b.precisao(45 - alvo.get('evasao', 0), usuario):
        bonus = random.randint(3, 5)
        usuario['evasao'] += bonus

def estrela_misteriosa(usuario, alvo):
    if b.precisao(55 - alvo.get('evasao', 0), usuario):
        estrela = random.randint(1, 4)
        match estrela:
            case 1:
                cura = b.cura(100, 200)
                cura = b.aumento_cura(usuario['cura_porcentagem'], cura)

                usuario['vida'] += cura
                b.limitar_vida(usuario)
            case 2:
                bonus = random.randint(8, 10)
                usuario['precisao_bonus'] += bonus
            case 3:
                usuario['dano_porcentagem'] += 0.25
            case 4:
                bonus = random.randint(3, 5)
                usuario['evasao'] += bonus

# ==========================================
#           ABSORVER SOL
# ==========================================

# Detalhes das Interações estão em interacoes.md

def absorver_sol(usuario, alvo):
    if b.precisao(5 - alvo.get('evasao', 0), usuario):
        usuario['vida'] *= 2
        usuario['vida_maxima'] *= 2
        usuario['precisao_bonus'] += 20
        b.limitar_vida(usuario)
