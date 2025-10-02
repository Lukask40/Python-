import os

# Limpar a tela (Windows)
os.system("cls")

# Listas para armazenar os pedidos
lista_pratos = []
lista_precos = []

while True:
    print("""
===== MENU =====
Código       Prato            Valor
  1         Picanha         R$ 25,00
  2         Lasanha         R$ 20,00      
  3         Strogonoff      R$ 18,00
  4         Bife acebolado  R$ 15,00
  5         Pão com ovo     R$ 5,00        
""")

    try:
        opcao = int(input("Digite o código da opção desejada: "))
    except ValueError:
        print("Entrada inválida. Digite um número.")
        continue

    match opcao:
        case 1:
            prato = "Picanha"
            preco = 25
        case 2:
            prato = "Lasanha"
            preco = 20
        case 3:
            prato = "Strogonoff"
            preco = 18
        case 4:
            prato = "Bife acebolado"
            preco = 15
        case 5:
            prato = "Pão com ovo"
            preco = 5
        case _:
            print("Opção inválida. Tente novamente...")
            os.system("pause")
            os.system("cls")
            continue

    # Armazenar o prato e preço nas listas
    lista_pratos.append(prato)
    lista_precos.append(preco)

    print(f"Você escolheu: {prato} - R$ {preco:.2f}")

    mais_pedidos = input("Deseja fazer um novo pedido? (S/N): ").upper()

    os.system("cls")

    if mais_pedidos == "N":
        break

# Mostrar a nota fiscal simples
print("\n======== NOTA FISCAL ========")
preco_total = 0
for i in range(len(lista_pratos)):
    print(f"{lista_pratos[i]} - R$ {lista_precos[i]:.2f}")
    preco_total += lista_precos[i]

print("=============================")
print(f"Total a pagar: R$ {preco_total:.2f}")






# OUTRO JEITO
# import os
# os.system("cls")

# lista_pratos = []
# precos_pratos = []

# while True:
#     opcao = int(input("""
# Código       Prato          Valor
#    1        Picanha         R$ 25,00
#    2        Lasanha         R$ 20,00
#    3        Strogonoff      R$ 18,00
#    4        Bife acebolado  R$ 15,00
#    5        Pão com ovo     R$ 5,00
                     
# Digite a opção desejada: """))
   
#     match opcao:
#         case 1:
#             prato = "Picanha"
#             preco = 25
#         case 2:
#             prato = "Lasanha"
#             preco = 20
#         case 3:
#             prato = "Strogonoff"
#             preco = 18
#         case 4:
#             prato = "Bife acebolado"
#             preco = 15
#         case 5:
#             prato = "Pão com ovo"
#             preco = 5
#         case _:
#             print("Opção inválida. \nTente novamente.\n")
   
#     if opcao >= 1 and opcao <= 5:
#         lista_pratos.append(prato)
#         precos_pratos.append(preco)

#     continuar = input("Deseja escolher outro prato? \nResponda com S ou N: ").lower()
#     if continuar == "n":
#         break
#     os.system("cls")

# if sum(precos_pratos) == 0:
#     print("\nNenhum prato foi escolhido")
# else:
#     print("\n= PRATOS ESCOLHIDOS=")
#     for prato in lista_pratos:
#         print(f"Prato: {prato}")

#     print(f"\nTotal: R$ {sum(precos_pratos):.2f}")

# print("\nVolte sempre!")