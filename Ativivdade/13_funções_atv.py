import os
os.system("cls")


lista_notas = []
def calculo(lista_notas):
   resultado = sum(lista_notas) / 3
   return resultado


for i in range(3):
     nota = int(input("Digite uma nota: "))
     lista_notas.append(nota)

media = calculo(lista_notas)

print(f"A média é {media}")
   


