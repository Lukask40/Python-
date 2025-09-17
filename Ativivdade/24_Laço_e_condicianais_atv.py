import os
os.system("cls")

QUANTIDADE_NOTAS = 3 # Uma costante
soma = 0

for i in range(QUANTIDADE_NOTAS):
 nota = int(input(f"Digite a {i+1}º nota: "))
 soma = soma + nota
 media = soma / 3


print(f"Média: {media}")

if media < 0 or media > 10:
    print("Média ivalida, insira novamente1")

if media >= 7:
     print("Aprovado")
elif media >= 5 or media <= 6.9:
     print("Recuperação")
else:
    print("Reprovado")




