import os
os.system("cls")

print(""" \t Comando \t\t Codigo
             CRIAR     \t    1
             Ler       \t    2
             Modificar \t    3
             Excluir   \t    4
           
""")
lista_clientes = []
codigo = int(input("Digite o codigo: "))

match codigo:
    case 1:
        nome = input("Digite seu nome: ")
        lista_clientes.append(nome)
        print(f"O nome: {nome} foi inserido com sucesso!")
        
    case 2:
        print("")
    case 3:
        print("")
    case 4:
         print("")
    case 5:
         print("")
    case _:
         print("Código invalido")