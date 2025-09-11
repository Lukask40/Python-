import streamlit as st
import time

st.title("Atividade")

st.header("Contagem regressiva")

st.write("Escrever um algoritmo que solicite ao usuário um número e faça a contagem regressiva a partir do número informado até o número 1, aguardando um segundo para exibir cada número. ")

n = st.number_input("Digite um número: ", step=1, min_value=0)

if st.button("Inicar"):
    for i in range(n, 0, -1):
         st.info(i)
         time.sleep(1)
        
else:
    st.warning("Digite um número!")

