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


if numero1 > numero2:
    maior = numero1
    menor = numero2
else:
    maior = numero2
    menor = numero1

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
