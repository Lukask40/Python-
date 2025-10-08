import os
os.system("cls")


def conversor(data):
  calcular = 2025 - data
  return calcular

data = int(input("Imforme sua data de nascimento: "))

idade = conversor(data)

print(f"Idade: {idade} anos.")