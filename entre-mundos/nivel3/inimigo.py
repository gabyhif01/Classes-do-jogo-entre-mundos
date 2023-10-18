import random

class InimigoEspacial:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, jogador):
        dano = random.uniform(5, self.ataque)
        jogador.vida -= dano

    def levar_dano(self, dano):
        self.vida -= dano

if __name__ == "__main__":
    inimigo1 = InimigoEspacial("Alien", 50, 10)
    inimigo2 = InimigoEspacial("Robô", 60, 12)

    jogador_vida = 100

    while jogador_vida > 0 and (inimigo1.vida > 0 or inimigo2.vida > 0):
        if inimigo1.vida > 0:
            inimigo1.atacar(jogador_vida)
        if inimigo2.vida > 0:
            inimigo2.atacar(jogador_vida)

      
    if jogador_vida <= 0:
        print("O jogador foi derrotado.")
