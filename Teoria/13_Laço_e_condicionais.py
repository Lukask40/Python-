import streamlit as st
import time


st.title("Atividade")

st.header(" Verificando pares e ímpares")

st.write("Escreva um algoritmo que solicite ao usuário 5 valores inteiros e ao final mostre: quantos números são pares, quantos números são ímpares.")

pares = 0
impares = 0

n1 = st.number_input("Digite o primeiro número: ", step=1)
n2 = st.number_input("Digite o segundo número: ", step=1)
n3 = st.number_input("Digite o terceiro número: ", step=1)
n4 = st.number_input("Digite o quarto número: ", step=1)
n5 = st.number_input("Digite o quinto número: ", step=1)


if st.button("Iniciar"):
    for numero in [n1, n2, n3, n4, n5]:


     if numero % 2 == 0:
        pares + 1
     else:
        impares + 1
        
    
else:
     st.info("Informe os números")



st.success(f"Quantidade de números pares: {pares}")
st.success(f"Quantidade de números ímpares: {impares}")



# outro jeio
#import streamlit as st
#st.title("Verificando pares e impares")
#pares = 0
#impares = 0
#for i in range(1,6):
#numero st.number_input(f"Digite o {i}º número: ", step=1)
#if numero % 2 == 0:
#pares pares + 1
#else:
#impares impares + 1
#if st.button("Verificar"):
#st.info (f"Quantidade de pares: (pares]")
#st.info(f"Quantidade de impares: (impares)")
