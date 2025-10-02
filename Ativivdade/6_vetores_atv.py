import os
os.system("cls")

lista_numero = []

qtd_pares = 0
qtd_impares = 0

for i in range(6):
    numero = int(input(f"Digite o {i+1}ª número: "))
    lista_numero.append(numero)
    if numero % 2 == 0:
        qtd_pares += 1
        
    else:
        qtd_impares += 1

# for i in range (QUANTIDADE_NUMEROS):
# print(f"Número: {lista_numeros [i]}")
for numero in lista_numero:
    print(f"Número: {numero}")

print(f"Quantidade de números pares: {qtd_pares}")
print(f"Quantidade de números ímpares: {qtd_impares}")


print("FIM")