import streamlit as st
import time

st.title("Laço de repetição - FOR.")

st.header("Contagem.")

numero = st.number_input("Digite até onde quer o laço de repetição: ", step=1)

if st.button("Iniciar"):
    for i in range(1,numero+1):
        st.info(i)
        time.sleep(1)
    st.header("FIM")