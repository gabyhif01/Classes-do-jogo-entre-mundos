class Carro:
  def __init__(self, nome, potencia, velocidade, preco):
      self.nome = nome
      self.potencia = potencia
      self.velocidade = velocidade
      self.preco = preco
     
# Definir os quatro tipos de carros
carro1 = Carro("UNO", 119, 140,"R$22.500,00" )
carro2 = Carro("SUV", 300, 180, "R$119.990,00")
carro3 = Carro("BMW i8", 374, 250, "R$ 710.950,00")
carro4 = Carro("Bugatti Chiron", 1.600 , 440, "R$ 48.735.314")

# Função para exibir as especificações de um carro
def exibir_especificacoes(carro):
  print(f"Nome: {carro.nome}")
  print(f"Potência do Motor: {carro.potencia} cavalos")
  print(f"Velocidade Máxima: {carro.velocidade} km/h")
  print(f"Preço : {carro.preco}")
  print()

# Menu de seleção de carros
while True:
  print("Selecione um carro:")
  print("1. UNO")
  print("2. SUV")
  print("3. BMW i8")
  print("4. Bugatti Chiron")
  print("0. Sair")

  escolha = input("Digite o número do carro desejado: ")

  if escolha == '1':
      exibir_especificacoes(carro1)
  elif escolha == '2':
      exibir_especificacoes(carro2)
  elif escolha == '3':
      exibir_especificacoes(carro3)
  elif escolha == '4':
      exibir_especificacoes(carro4)
  elif escolha == '0':
      break
  else:
      print("Escolha inválida. Por favor, escolha um número de carro válido.")
