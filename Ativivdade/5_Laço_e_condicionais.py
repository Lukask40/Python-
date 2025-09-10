# verificando a média
# Solicite ao usuário a média do aluno
# Se maior ou igual a 7, mostre como aprovado
# Caso contrário, mostre como reprovado.

import streamlit as st

st.title("Verificando a média.")

media= st.number_input("Digite a sua média: ")

if st.button("Verificar"):
    if media >= 7:
        st.success("Aprovado!")
    else:
        st.error("Reprovado!")
else:
    st.info("Imforme a média.")


# success = verde
# warning = amarelo
# info = azul
# erro = vermelho
