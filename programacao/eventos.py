import random


def aplicar_evento_terceira_lua(usuario, alvo, evento):
    # Aplica um dos efeitos aleatorios da Terceira Lua

    match evento:
        case 1:
            usuario['dano_porcentagem'] += 0.35
        case 2:
            usuario['evasao'] += 4
        case 3:
            usuario['cura_porcentagem'] += 0.50
        case 4:
            usuario['precisao_bonus'] += 8
        case 5:
            alvo['veneno'] *= 2
            usuario['resistencia'] *= 2
            usuario['plumas'] *= 2


def terceira_lua(personagem1, personagem2):
    # Sorteia e aplica o evento da Terceira Lua aos personagens ativos

    evento = random.randint(1, 5)

    if personagem1.get('terceira_lua', False):
        aplicar_evento_terceira_lua(personagem1, personagem2, evento)

    if personagem2.get('terceira_lua', False):
        aplicar_evento_terceira_lua(personagem2, personagem1, evento)


def TerceiraLua(personagem1, personagem2):
    # Aplicar a terceira lua final

    terceira_lua(personagem1, personagem2)
