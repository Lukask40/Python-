import os 
os.system("cls")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media < 7:
    status = "Reprovado"
else:
    status = "Aprovado"

print(f"Média: {media:.2f}")
print(f"Situação: {status}")
