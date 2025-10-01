import os
os.system("cls")

lista_notas = []

for i in range(4):
    nota = int(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)


soma = sum(lista_notas)
media = soma / 4



for i in range(4):
    print(f"Nota: {lista_notas[i]}")

print(f"Soma:  {soma}")
print(f"Média:  {media}")

if media < 0 or media > 10:
    print("Média ivalida, insira novamente1")

if media >= 7:
     print("Aprovado")
elif media >= 5:
     print("Recuperação")
else:
    print("Reprovado")





print("FIM")