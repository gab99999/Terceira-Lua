import random

def dano (min, max):
    return random.randint (min, max)

def precisao(pontos):
    x = random.randint (1, 100)
    if x <= pontos:
        return True
    else:
        return False


