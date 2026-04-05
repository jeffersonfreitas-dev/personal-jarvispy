import streamlit as st

st.set_page_config(page_title="Meu Hello World", page_icon="👋")

st.title("Hello, World! 👋")
st.write("Meu primeiro app no Streamlit Community Cloud!")

nome = st.text_input("Qual o seu nome?")

if nome:
    st.success(f"Olá, {nome}! Seja bem-vindo 🎉")