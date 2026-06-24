from personagens import personagens as skill
import random

escolha1 = 'Amara'
escolha2 = 'Perfídia'

personagem1 = skill[escolha1]
personagem2 = skill[escolha2]

vida1 = personagem1['vida']
vida2 = personagem2['vida']

evasao1 = personagem1['evasao']
evasao2 = personagem2['evasao']

curaporcentagem1 = 0
danoporcentagem1 = 0

curaporcentagem2 = 0
porcentagem2 = 0

curapontual1 = 0
danopontual1 = 0

curapontual2 = 0
danopontual2 = 0

precisaopontual1 = 0
evasaopontual1 = 0

precisaopontual2 = 0
evasaopontual2 = 0

print(personagem1)

while vida1 > 0 and vida2 > 0:
