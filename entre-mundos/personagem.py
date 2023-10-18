import random

class Jogador:
  def __init__(self, nome, HP): 
    self.nome = nome
    self.HP = HP
    self.vida = 3

  def perde_vida(self):
    self.vida -= random.randint(0,1)
    if self.vida <= 0:
      return "game over!"
      r = str(input("Deseja reiniciar o jogo?"))
      while True:
        if r== "sim":
          pass
        else:
          break
  def ganha_vida(self):
    self.vida += random.randint(1,3)
    