import os
os.system("cls")

print("Laço de repetição")

QUANTIDADES_NOTAS = 2
soma = 0
 
for i in range(QUANTIDADES_NOTAS):
    while True:
      nota = int(input (f"Digite a {i+1}º nota: "))
      if nota >= 0 and nota <= 10:
         break
    soma = soma + nota

media = soma / QUANTIDADES_NOTAS

print(f"Média: {media}")





