import os
os.system("cls")

idade = int(input("Digite a idade: "))

if idade >= 18 and idade <= 65:
    print("Voto obrigatório.")
else:
    print("Voto não obrigatório.")