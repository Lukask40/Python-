import os
os.system("cls")

print(""" \t Prato \t\t valor
Picanha \t R$ 25,00
Lasanha \t R% 20,00
Strogonoff \t R$ 18,00
Bife acebolado \t R$ 20,00
Pão com ovo \t R$ 5,00
""")

codigo = int(input("Digite o primeiro número: "))

match codigo:
    case 1:
        print("Picanha,valor:R$ 25,OO reais")
    case 2:
        print("Lasanha,valor:R$ 20,OO reais")
    case 3:
        print("Strogonoff,valor:R$ 18,OO reais")
    case 4:
         print("Bife acebolado,valor:R$ 20,OO reais")
    case 5:
         print("Pão com ovo,valor:R$ 5,OO reais")
    case _:
         print("Código invalido")