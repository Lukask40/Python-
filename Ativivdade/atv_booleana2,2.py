import os
os.system("cls")

idade = int(input("Digite sua idade: "))


if idade < 18 or idade > 65:
  print("Não é obrigado a votar.")
else:
  print("Obrigado a votar!")