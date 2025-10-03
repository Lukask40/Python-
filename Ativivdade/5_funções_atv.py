import os
os.system("cls")

#Função com passagem de parametros.
#Parametros são os que ta dento dos parenteses.

# Criando uma função.
def saudacao (nome, idade, altura, peso):
  print(f"Olá, {nome}! Bem-vindo(a)!")
  print(f"Sua idade é {idade} anos.")
  print(f"Sua altura é {altura} metros.")
  print(f"Seu peso é {peso}.")

print("Solicitando dados.")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = int(input("Digite seu peso: "))

# Chamando a função.
os.system("cls")
saudacao (nome, idade, altura, peso)


