import streamlit as st


st.title("Atividade")

st.header(" Verificando a média")

st.write("Escrever um programa de computador que solicite do usuário 4 notas e, ao final, apresente a média.")

QUANTIDADE_NOTAS = 3 # Uma costante
soma = 0

for i in range(QUANTIDADE_NOTAS):
 nota = st.number_input (f"Digite a {i+1}º nota: ", step=1)
 soma = soma + nota
 media = soma / 3

if st.button("Resultado"):
  st.info(f"Média: {media}")

  if media >= 7:
     st.success("Aprovado")
  elif media >= 4.1 and media <= 6.8:
     st.warning("Recuperação")
  else:
    st.error("Reprovado")


else:
  st.warning("Insira as notas.")




