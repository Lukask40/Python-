import streamlit as st
import time

st.title("Contagem de 1 até 20 ímpares")

st.header("Contagem.")

if st.button("Iniciar"):
    for i in range( 1,21, 2):
        st.info(i)
        time.sleep(1)
    st.header("FIM")