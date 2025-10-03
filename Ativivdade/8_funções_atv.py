import os
os.system("cls")


def saudacao (numero):
 for i in range(1, 11):
    print(f"{numero} x {i} = {i * numero}")
  
numero = int(input("Digite um número: "))

saudacao(numero)
         