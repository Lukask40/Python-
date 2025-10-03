import os
os.system("cls")



def saudacao (numero, pares, impares):
 print(f"Número digitado: {numero}")
 if numero == pares:
  print(f"{pares}  número é par")
 else:
  print(f" {impares} Esse número é impar.")

numero = int(input("Digite um número: "))
pares = int
impares = int

if numero % 2 == 0:
    pares = numero
        
else:
    impares = numero

saudacao(numero, pares, impares)