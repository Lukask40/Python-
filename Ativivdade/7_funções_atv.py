import os
os.system("cls")



def saudacao (numero, negativo, positivo):
 print(f"Número digitado: {numero}")
 if numero == negativo:
  print(f"{negativo} Esse número é negativo")
 else:
  print(f" {positivo} Esse número é positvo.")

numero = int(input("Digite um número: "))
positivo = int
negativo = int


if numero < 0:
    negativo = numero
        
else:
    positivo = numero

saudacao(numero, negativo, positivo)