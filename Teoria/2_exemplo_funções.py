
import os
import time
os.system("cls")

# função sem parâmetros e sem retorno.
def limpa_tela():
 print("Boa tarde!")
 time.sleep(3) # Espera 3 segundos.
 os.system("cls")

# Função para somar com parâmetros e com retorno.
def calcular_media(n1, n2):
  calcular = n1 + n2 / 2
  return calcular

 # Função com parâmetros e sem retorno
def mostrar_resultado(media):
  print(f"Resultado: {media}")
  if media >= 7:
    print("Aprovado!")
  else:
    print("Reprovado!")

# Código principal.
limpa_tela() # Chamando a função.

primeiro_numero = int(input("Digite um numero:"))
segundo_numero = int(input("Digite um numero:"))

# Função para somar com parâmetros e com retorno.
media = calcular_media(primeiro_numero, segundo_numero)

# Função com parâmetros e sem retorno.
mostrar_resultado(media) #chamando a função.