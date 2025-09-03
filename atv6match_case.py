import os
os.system("cls")

sexo = input("Insira o seu sexo: ")
altura = float(input("Insira sua altura: "))
peso = float(input("Insira seu peso: "))

match sexo:
    case "M":
        calculo = peso * altura - 58
        print(f"O peso ideal seria: {calculo}")
    case "F":
        calculo = peso * altura - 44.7
        print(f"O peso ideal seria: {calculo}")


