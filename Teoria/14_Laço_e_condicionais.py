import streamlit as st


st.title("Atividade")

st.header(" Verificando a média")

st.write("Escrever um programa de computador que solicite do usuário 4 notas e, ao final, apresente a média.")


soma = 0

for i in range(4):
 nota = st.number_input (f"Digite a {i+1}º nota: ", step=1)
 soma = soma + nota
 media = soma / 4

if st.button("Resultado"):
  st.success(f"Média: {media}")

else:
  st.warning("Insira as notas.")




