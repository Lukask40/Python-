import os
os.system("cls")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operador = input("Digite um operador(+,-,*,/): ")


match operador:
    case "+":
        resultado = n1 + n2
    case "-":
        resultado = n1 - n2
    case "*":
        resultado = n1 * n2
    case "/":
        resultado = n1 / n2
    case _:
        resultado = "Operador invalido"

print(f"Números: {n1} e {n2}")
print(f"Operador escolhido: {operador}")
print(f"Resultado: {resultado}")    
