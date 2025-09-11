import streamlit as st
import time

st.title("Tabuada")

st.header("Aprendendo a tabuada ")

n = st.number_input("Digite um número: ")

if st.button("Inicar multiplicação"):
    for i in range(1, 11):
         st.info(n * i)
         time.sleep(1)
        
else:
    st.info("Digite um número!")





   
    
