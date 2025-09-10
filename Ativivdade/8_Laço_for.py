import streamlit as st
import time

st.title("Laço de repetição - FOR.")

st.header("Contagem.")

if st.button("Iniciar"):
    for i in range( 100,121, 2):
        st.info(i)
        time.sleep(1)
    st.header("FIM")