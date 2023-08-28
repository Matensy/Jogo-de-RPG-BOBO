# Função para gerar número aleatório
def gerar_numero(seed, maximo):
    seed = (seed * 32719 + 3) % 32749
    return (seed % maximo) + 1, seed

# Simular ataque
def atacar(atacante, arma):
    if arma == "ESPADA":
        return gerar_numero(atacante, 10)
    elif arma == "KATANA":
        return gerar_numero(atacante, 12)
    elif arma == "ESCUDO":
        return gerar_numero(atacante, 8)
    elif arma == "ARCO":
        return gerar_numero(atacante, 8)

# Personagens e armas
personagens = {
    "GUERREIRO": {"hp": 80, "arma": "ESPADA"},
    "ESPADACHIM": {"hp": 60, "arma": "KATANA"},
    "TANQUE": {"hp": 100, "arma": "ESCUDO"},
    "ARQUEIRO": {"hp": 70, "arma": "ARCO"}
}

# Escolha uma ação
def escolher_acao(jogador):
    print(f"\nEscolha uma ação para {jogador['classe']}:")
    print("1. Ataque Normal")
    print("2. Ataque Forte")
    print("3. Ataque Especial")
    print("4. Curar")
    return int(input())

# Turno de combate
def turno_combate(jogador1, jogador2):
    print(f"\nTurno de {jogador1['classe']}")
    acao = escolher_acao(jogador1)

    if acao == 1:
        dano = atacar(jogador1['hp'], jogador1['arma'])[0]
        jogador2['hp'] -= dano
        print(f"{jogador1['classe']} causou {dano} de dano a {jogador2['classe']}!")
    elif acao == 2:
        dano = atacar(jogador1['hp'], jogador1['arma'])[0] * 2
        jogador2['hp'] -= dano
        print(f"{jogador1['classe']} causou {dano} de dano a {jogador2['classe']}!")
    elif acao == 3:
        if jogador1['classe'] == "ARQUEIRO":
            dano = atacar(jogador1['hp'], jogador1['arma'])[0] * 1.5
            jogador2['hp'] -= dano
            print(f"{jogador1['classe']} usou um ataque especial e causou {dano} de dano a {jogador2['classe']}!")
        else:
            print("Ataque especial não disponível para esta classe.")
    elif acao == 4:
        if jogador1['classe'] == "TANQUE":
            jogador1['hp'] += 20
            print(f"{jogador1['classe']} se curou em 20 pontos de vida!")
        else:
            print("Curar não disponível para esta classe.")
    else:
        print("Ação inválida. Passe a vez.")

# Início do combate
print("Bem-vindo ao Simulador de Batalha de RPG!")

# Escolha o jogador
print("\nEscolha sua classe:")
for classe in personagens:
    print(classe)
classe_jogador = input().upper()
arma_jogador = personagens[classe_jogador]["arma"]

jogador = {
    "classe": classe_jogador,
    "hp": personagens[classe_jogador]["hp"],
    "arma": arma_jogador
}

# Escolha amigo ou bot
print("\nDeseja jogar com um amigo? (1 - Sim / 2 - Não)")
opcao_amigo = int(input())

if opcao_amigo == 1:
    print("\nEscolha a classe do amigo:")
    for classe in personagens:
        print(classe)
    classe_amigo = input().upper()
    arma_amigo = personagens[classe_amigo]["arma"]

    amigo = {
        "classe": classe_amigo,
        "hp": personagens[classe_amigo]["hp"],
        "arma": arma_amigo
    }
else:
    seed = int(input("\nDigite uma semente numérica: "))
    classe_bot = list(personagens.keys())[seed % len(personagens)]
    arma_bot = personagens[classe_bot]["arma"]

    amigo = {
        "classe": classe_bot,
        "hp": personagens[classe_bot]["hp"],
        "arma": arma_bot
    }

# Início do combate
print("\nComeça a batalha!")
turno = 1
while jogador["hp"] > 0 and amigo["hp"] > 0:
    print(f"\nTurno {turno}")
    turno_combate(jogador, amigo)
    if amigo["hp"] <= 0:
        break
    turno_combate(amigo, jogador)
    if jogador["hp"] <= 0:
        break
    turno += 1

# Resultado final
if jogador["hp"] > 0:
    print("Você venceu a batalha!")
else:
    print("Você foi derrotado. Tente novamente!")
