import random

class PersonagemEspacial:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.gravidade = random.uniform(0.1, 0.5)  
        self.stamina = 100  

    def andar(self):
        if self.vida <= 0:
            print(f"{self.nome} está sem energia e não pode andar.")
            return

        gasto_energia = random.uniform(0.1, 0.5)
        self.stamina -= gasto_energia
        self.vida -= gasto_energia

        if self.stamina <= 0:
            print(f"{self.nome} está exausto e não pode mais andar.")
            self.stamina = 0

        if self.vida <= 0:
            print(f"{self.nome} ficou sem vida e não pode mais andar.")

    def explorar_planeta(self):
        while self.vida > 0:
            self.andar()

        print(f"{self.nome} desmaiou de exaustão.")

if __name__ == "__main__":
    personagem = PersonagemEspacial("Astronauta")
    personagem.explorar_planeta()
