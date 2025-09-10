import streamlit as st
 
st.title("Calculadora!")

n1 = st.number_input("Digite o primeiro número: ")
n2 = st.number_input("Digite o segundo número: ")

soma = n1 + n2 
media = soma / 2
produto = n1 * n2

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

if st.button("Resultados"):
    st.write(f"Soma: {soma}")
    st.write(f"Média: {media}")
    st.write(f"Produto: {produto}")
    st.write(f"Maior: {maior}")
    st.write(f"Menor: {menor}")
else:
    st.info("Digite os números!")


# maior = max(n1, n2)
# menor = min(n1, n2)
    
