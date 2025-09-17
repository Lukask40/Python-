import streamlit as st

st.title("Login e senha")

st.write("Crie um programa que solicite ao usuário seu login e uma senha. O programa deve continuar pedindo o login e a senha até que ambos estejam corretos. O programa deve solicitar o login e senha apenas três vezes. Caso ultrapasse o número de tentativas, o programa deve ser finalizado.")

login_correto = "adm"
senha_correta = "123"

st.session_state.setdefault("campo", False)
st.session_state.setdefault("tentativas", 0)

login = st.text_input("Digite seu login: ", disabled=st.session_state.campo)
senha = st.text_input("Digite sua senha: ", type= "password", disabled=st.session_state.campo)

if st.button("Entrar"):
    if login == login_correto and senha == senha_correta:
        st.success("Login realizado com sucesso!")
    else:
        st.session_state.tentativas +=1
        if st.session_state.tentativas <= 3:
            st.error(f"login ou senha incorreto, tentativas: {st.session_state.tentativas}")
        else:
            st.session_state.campo = True
            st.error("Númro de tentativas ínvalidas")


