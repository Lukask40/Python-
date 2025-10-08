import os
import time
os.system("cls")

# função sem parâmetros e sem retorno.
def limpa_tela():
 print("Boa tarde!")
 time.sleep(3) # Espera 3 segundos.
 os.system("cls")

# Função para somar com parâmetros e com retorno.
def calcular_soma(n1, n2):
  calcular = n1 + n2 
  return calcular
def calcular_multiplicacao(n1, n2):
  calcular = n1 * n2
  return calcular
def calcular_subtracao(n1, n2):
  calcular = n1 - n2 
  return calcular
def calcular_divisao(n1, n2):
  # return n1 / n2 if n2 != 0 else "Divisão por zero.
 #if n2 == 0:
  #print("Divisão por zero.")
 #else:
  #return n1/n2
  calcular = n1 / n2 
  return calcular

 # Função com parâmetros e sem retorno
def mostrar_resultado(soma, multiplicacao, subtracao, divisao):
  print("====RESULTADOS====")
  print(f"Soma: {soma}")
  print(f"Multiplicação: {multiplicacao}")
  print(f"Subtação: {subtracao}")
  print(f"Divisão: {divisao}")
  

# Código principal.
limpa_tela() # Chamando a função.

primeiro_numero = int(input("Digite um numero:"))
segundo_numero = int(input("Digite um numero:"))

# Função para somar com parâmetros e com retorno.
soma = calcular_soma(primeiro_numero, segundo_numero)
multiplicacao = calcular_multiplicacao(primeiro_numero, segundo_numero)
subtracao = calcular_subtracao(primeiro_numero, segundo_numero)
divisao = calcular_divisao(primeiro_numero, segundo_numero)

# Função com parâmetros e sem retorno.
mostrar_resultado(soma, multiplicacao, subtracao, divisao) #chamando a função.