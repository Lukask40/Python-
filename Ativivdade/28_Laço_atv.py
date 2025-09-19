import os
os.system("cls")
qtd_pares = 0
qtd_impares = 0
soma_pares = 0
soma_total = 0
qtd_total = 0

while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    soma_total += numero
    qtd_total += 1
    if numero % 2 == 0:
        qtd_pares += 1
        soma_pares += numero
    else:
        qtd_impares += 1

print(f"Quantidade de números pares: {qtd_pares}")
print(f"Quantidade de números ímpares: {qtd_impares}")

if qtd_pares > 0:
    print(f"Média dos valores pares: {soma_pares / qtd_pares:.2f}")
else:
    print("Não foram digitados números pares.")

if qtd_total > 0:
    print(f"Média geral dos números: {soma_total / qtd_total:.2f}")
else:
    print("Nenhum número foi digitado.")