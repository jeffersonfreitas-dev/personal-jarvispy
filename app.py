import streamlit as st
from components.auth import require_login

st.set_page_config(page_title="JarvisPy", layout="wide", page_icon="🏠")

name, username = require_login()

st.title(f"Bem-vindo, {name} 👋")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Saldo Total", "R$ 8.450", "+R$ 320 este mês")

with col2:
    st.metric("Carteira de Ações", "R$ 12.300", "+2,4%")

with col3:
    st.metric("Notícias não lidas", "14", "3 novas")