import os
os.system("cls")


def conversor(valor):
  if valor < 100:
   calcular = valor * 1.10
   return calcular
  else:
   calcular = valor * 1.20
   return calcular

valor = float(input("Imforme o preço do produto: "))

valor_ajustado = conversor(valor)

print(f"Novo preço: {valor_ajustado:.2f}.")