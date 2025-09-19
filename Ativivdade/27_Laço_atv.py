import os
os.system("cls")

soma = 0
contador = 0


while True:
    nota = int(input("Digite uma nota: "))
    if nota < 0:
       break
    soma += nota
    contador += 1


media = soma / contador

print(f"A média aritmética é: {media:.2f}")
