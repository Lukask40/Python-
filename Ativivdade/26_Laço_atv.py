import os
os.system("cls")

soma = 0
contador = 0

while True:
    nota = float(input("Digite uma nota: "))
    soma += nota
    contador += 1

    opcao = input("Deseja inserir mais uma nota? (S/N): ").upper()
    if opcao == "N":
        break

media = soma / contador
print(f"\nForam digitadas {contador} notas.")
print(f"A média aritmética é: {media:.2f}")