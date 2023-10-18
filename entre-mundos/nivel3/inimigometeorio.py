import random
from personagem import  PersonagemEspacial as  PersonagemEspacial

class Meteoro:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano

    def cair(self, jogador):
        dano = random.uniform(10, self.dano)
        jogador.vida -= dano
        print(f"O meteoro {self.nome} atingiu {jogador.nome}, causando {dano} de dano!")

if __name__ == "__main__":
    # Exemplo de uso da classe Meteoro
    jogador = PersonagemEspacial("Astronauta")
    meteoro1 = Meteoro("Pequeno", 20)
    meteoro2 = Meteoro("Grande", 40)

    # Simulação de meteoros caindo
    jogador_vida = 100

    while jogador_vida > 0:
        meteoro = random.choice([meteoro1, meteoro2])
        meteoro.cair(jogador)

        if jogador.vida <= 0:
            print(f"{jogador.nome} foi atingido por um meteoro e não sobreviveu.")
            break
