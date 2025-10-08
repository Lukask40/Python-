import os
os.system("cls")


def conversor(numero):
  calcular = numero * 100
  return calcular

def mostrar_resultado(centimetros):
  print(f"{centimetros} centimetros.")
  
numero = int(input("Digite um numero:"))
print(f"Número informado: {numero} metros.")

centimetros = conversor(numero)

mostrar_resultado(centimetros)


# Menos linha e uma função
# import os
# os.system("cls")

# def calcular_e_mostrar(numero):
#     centimetros = numero * 100
#     print(f"Número informado: {numero} metros.")
#     print(f"{centimetros} centímetros.")
#     return centimetros  # Retorna o valor convertido

# # Entrada do usuário
# numero = int(input("Digite um número: "))
# resultado = calcular_e_mostrar(numero)  # Guarda o valor retornado, se quiser usar depois
