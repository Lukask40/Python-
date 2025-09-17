import streamlit as st


st.title("Lacos de repetição.")

st.write("Crie um programa que solicite ao usuário seu login e uma senha. O programa deve continuar pedindo o login e a senha até que ambos estejam corretos.")

login_correto = "adm"
senha_correta = "123"

login = st.text_input("Digite seu login: ")
senha = st.text_input("Digite sua senha: ", type= "password")

if st.button("Entrar"):
    if login == login_correto and senha == senha_correta:
        st.success("Login realizado com sucesso!")
    else:
        st.error("login ou senha incorreto!")


