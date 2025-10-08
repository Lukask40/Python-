
import os
import time
os.system("cls")

# função sem parâmetros e sem retorno.
def limpa_tela():
 print("Boa tarde!")
 time.sleep(3) # Espera 3 segundos.
 os.system("cls")

# Função para somar com parâmetros e com retorno.
def somar(n1, n2):
  calcular = n1 + n2
  return calcular

 # Função com parâmetros e sem retorno
def mostrar_resultado(soma):
  print(f"Resultado: {soma}")

# Código principal.
limpa_tela() # Chamando a função.

primeiro_numero = int(input("Digite um numero:"))
segundo_numero = int(input("Digite um numero:"))

# Função para somar com parâmetros e com retorno.
soma = somar(primeiro_numero, segundo_numero)

# Função com parâmetros e sem retorno.
mostrar_resultado(soma) #chamando a função.