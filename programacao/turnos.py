import random
from personagens import personagens
import IA_dos_bots
import IA_chefao

class Personagem:
    def __init__(self, nome, hp, ataque):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque
        self.vivo = True
        

    def atacar(self, alvo):
        alvo.hp -= self.ataque
        print(f"{self.nome} atacou {alvo.nome}! {alvo.hp} HP restante.")
        if alvo.hp <= 0:
            alvo.vivo = False
            print(f"{alvo.nome} foi derrotado!")
        else:
            alvo.vivo = True
            print(f"{alvo.nome} está com {alvo.hp} HP restante.")

#Aguardando a integração com IA para o INIMIGO
class Inimigo:
    def inimigo(self, nome, hp, ataque):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque
        self.vivo = True
    
    IA_dos_bots
    IA_chefao
    
class SistemaTurnos:
    def __init__(self, personagem1, personagem2):
        self.combatentes = [personagem1, personagem2]
        self.turno = 0

    def jogador_atual(self):
        return self.combatentes[self.turno]

    def alvo_atual(self):
        return self.combatentes[1 - self.turno]

    def proximo_turno(self):
        self.turno = 1 - self.turno

    def combate_acabou(self):
        return (
            self.combatentes[0]["vida"] <= 0 or
            self.combatentes[1]["vida"] <= 0
        )

    def vencedor(self):
        if self.combatentes[0]["vida"] > 0:
            return self.combatentes[0]
        return self.combatentes[1]

# Configuração inicial ainda será alterada
player = Personagem("Jogador", 100, 10)
inimigo = Inimigo("Demônio", 50, 5)
combatentes = [player, inimigo]
turno = 0

print("Início do Combate!\n")

# Loop principal de turnos
while player.vivo and inimigo.vivo:
    atacante = combatentes[turno % len(combatentes)]
    alvo = combatentes[(turno + 1) % len(combatentes)]

    print(f"--- Turno de {atacante.nome} ---")
    
    # Ações do turno
    if atacante == player:
        escolha = input("O que fazer? (1- Atacar) (2- Fugir) (3- Defender) (4- Usar Habilidade): ")
        if escolha == "1":
            atacante.atacar(alvo)
        elif escolha == "2":
            print(f"{atacante.nome} tentou fugir, mas não conseguiu!")
        elif escolha == "3":
            print(f"{atacante.nome} se defendeu!")
        elif escolha == "4":
            atacante.usar_habilidade(alvo) #Aguardando construção das habilidades
    else:
        atacante.atacar(alvo)

    print()
    turno += 1

# Fim do combate
vencedor = player if player.vivo else inimigo
print(f"Fim de jogo! {vencedor.nome} venceu a batalha!")
