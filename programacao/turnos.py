
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
