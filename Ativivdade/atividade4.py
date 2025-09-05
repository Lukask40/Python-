import os
os.system("cls")

numero1 = int(input("Digite o número: "))
numero2 = int(input("Digite o número: "))


media = (numero1 + numero2) / 2 
print(f"A média é: {media}")

soma = numero1 + numero2
print(f"A soma é: {soma}")

produto = numero1 * numero2
print(f"O produto é: {produto}")

if numero1 == numero2:
 print("Os números são iguis")
else:
  print("Os números são diferentes")