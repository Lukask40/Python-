import os
os.system("cls")

#Função com passagem de parametros.
#Parametros são os que ta dento dos parenteses.

# Criando uma função.
def saudacao (nome, idade):
  print(f"Olá, {nome}! Bem-vindo(a)!")
  print(f"Sua idade é {idade} anos.")

print("Solicitando dados.")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Chamando a função.
saudacao (nome, idade)


