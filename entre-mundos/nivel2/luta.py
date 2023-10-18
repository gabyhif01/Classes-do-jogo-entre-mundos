import random

class Personagem:
    def __init__(self, nome, hp, ataque, defesa):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        dano = random.randint(0, self.ataque)
        alvo.defender(dano)

    def defender(self, dano):
        dano_final = max(0, dano - self.defesa)
        self.hp -= dano_final
        print(f"{self.nome} defende e sofre {dano_final} de dano!")

    def esta_vivo(self):
        return self.hp > 0

class Monstro(Personagem):
    def __init__(self, nome, hp, ataque, defesa):
        super().__init__(nome, hp, ataque, defesa)

class Jogador(Personagem):
    def __init__(self, nome, hp, ataque, defesa):
        super().__init__(nome, hp, ataque, defesa)

def main():
    jogador = Jogador("Herói", 100, 20, 10)
    monstro = Monstro("Monstro", 80, 15, 5)

    while jogador.esta_vivo() and monstro.esta_vivo():
        jogador.atacar(monstro)
        if monstro.esta_vivo():
            monstro.atacar(jogador)

        print(f"{jogador.nome}: {jogador.hp} HP")
        print(f"{monstro.nome}: {monstro.hp} HP")
        print()

    if jogador.esta_vivo():
        print("Você derrotou o monstro!")
    else:
        print("Você foi derrotado pelo monstro!")

if __name__ == "__main__":
    main()
