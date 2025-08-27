import os 
os.system("cls")

maca = int(input("Digite quantas maçãs você quer: "))

if maca < 12:
    preco = 1.30
else:
    preco = 1.0

total = maca * preco

print(f"Você comprou {maca} maçãs e o valor total é R$ {total:.2f}")

