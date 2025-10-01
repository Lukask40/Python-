import os
os.system("cls")

lista_numeros = []

for i in range(5):
    n = int(input(f"Digite o {i+1}ª número: "))
    lista_numeros.append(n)



maior = max(lista_numeros)
menor = min(lista_numeros)

for i in range(5):
    print(f"Números digitados: {lista_numeros[i]}")



print(f"Maior: {maior}")
print(f"Menor: {menor}")



print("FIM")