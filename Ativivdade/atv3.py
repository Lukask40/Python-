import os 
os.system("cls")

nome = input("Digite seu nome: ")
nota1 = int(input("Digite a mota 1: "))
nota2 = int(input("Digite a nota 2: "))

soma = nota1  + nota2
media = soma / 2 

if media > 9:
    conceito = "A"
elif media > 7.5:
    conceito = "B"
elif media > 6: 
    conceito = "C"
elif media > 4:
    conceito = "D"
else:
    conceito = "E"

if conceito in ["A", "B","C"]:
    status = "Aprovado"
else:
    status = "Reprovado"


print(f"Aluno: {nome}")
print(f"Media: {media}")
print(f"Conceito: {conceito}")
print(f"Status: {status}")