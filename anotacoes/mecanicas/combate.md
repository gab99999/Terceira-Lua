# Mecânicas Base - Terceira Lua

## Estrutura da Partida

* Combate 1x1.
* Cada jogador realiza apenas 1 ação por turno.
* Partidas rápidas, com duração aproximada de 3 a 5 minutos.
* Objetivo: reduzir a vida do adversário a 0.

---

# Atributos

## Vida

Quantidade de vida do personagem.

Faixa prevista:

* Mínimo: 600
* Máximo: 1000

A vida varia conforme a proposta de cada personagem.

---

## Evasão

Representa a capacidade de evitar ataques.

Faixa prevista:

* 1 a 20 pontos

Funcionamento:

* A evasão reduz diretamente a precisão da habilidade utilizada contra o personagem.

Exemplo:

* Habilidade com 80 de precisão
* Inimigo com 10 de evasão

Precisão final:
80 - 10 = 70%

---

## Efeitos

Estados especiais aplicados por habilidades.

Exemplos:

* Marcas
* Queimadura
* Veneno
* Redução de precisão
* Aumento de evasão
* Outros efeitos exclusivos de personagens

---

# Sistema de Precisão

Todas as habilidades e interações possuem precisão.

Funcionamento:

1. Um número aleatório entre 1 e 100 é gerado.
2. O valor aparece visualmente dentro da Lua.
3. Se o valor for menor ou igual à precisão final:

   * Sucesso
4. Se o valor for maior:

   * Falha

Exemplo:

Precisão da habilidade:
80%

Número sorteado:
63

Resultado:
Sucesso

---

# Habilidades

Cada personagem possui:

* 1 Passiva
* 3 Habilidades

Características:

* Nenhuma habilidade será exclusivamente de cura.
* Habilidades podem causar dano e produzir efeitos adicionais.
* Habilidades podem possuir diferentes níveis de precisão.

Exemplos:

Golpe Astral

* 85 de dano
* Cura 20 de vida
* (Precisão = 80)

---

# Interações

Ações universais disponíveis para todos os personagens.

Também utilizam o sistema de precisão.

Exemplo:

Capturar Estrela

Escolha uma estrela presente no campo de batalha.

Possíveis efeitos:

* Recuperar vida
* Aumentar precisão
* Ganhar evasão
* Receber energia especial
* Outros bônus temporários

Cada efeito possui sua própria chance de sucesso.

Exemplos:

Capturar Estrela de Cura

* Recupera vida
* Precisão = 50

---

# Evento Global

## Chegada da Terceira Lua

Acontece por volta do turno 9.

Ao chegar:

* O cenário muda.
* O combate entra na fase final.
* Um efeito global aleatório é ativado.

Exemplos de efeitos:

* Aumento de dano global
* Redução da cura
* Aumento da precisão
* Aumento da evasão
* Aplicação de efeitos cósmicos
* Outros eventos especiais

Objetivo:
Criar uma fase final mais intensa e imprevisível.
