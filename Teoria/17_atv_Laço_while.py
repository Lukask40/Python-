import os
os.system("cls")

print("Laço de repetição - While")

while True:
    numero = int(input("Insira sua nota: "))
    if numero >= 0 and numero <= 10:
        break

print(f"Insira sua nota: {numero} ")