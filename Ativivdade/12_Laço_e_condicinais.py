import streamlit as st
 
st.title("Atividade!")

st.header("Somar 5 números")

st.write("Escrever um programa de computador que solicite do usuário 5 números inteiros e, ao final, apresente a soma de todos os números lidos.")

n1 = st.number_input("Digite o primeiro número: ", step=1)
n2 = st.number_input("Digite o segundo número: ", step=1)
n3 = st.number_input("Digite o terceiro número: ",step=1)
n4 = st.number_input("Digite o quarto número: ", step=1)
n5 = st.number_input("Digite o quinto número: ", step=1)

soma = n1 + n2 + n3 + n4 + n5


if st.button("Resultado"):
    st.success(f"Soma: {soma}")
  
else:
    st.error("Digite os números!")




# Outro jeito de fazer
# import streamlit as st
#  import time
# st.title("Atividade")
# st.header("Laço de repetição For")
#  st.write("Escrever um programa de computador que solicite do usuário 5 "
# "números inteiros e, ao final, apresente a soma de todos os números lidos.")
# soma = 0
# for i in range(1,6):
#  numero st.number_input(f"Digite o {i}º número: ", step=1, min_value=0)
#  soma soma + numero
#  time.sleep(1)
# if st.button("Iniciar"):
#  st.success(f"A soma do números é: (soma)")
#  else:
#  st.info("Informe um número")
