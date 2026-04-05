import streamlit_authenticator as stauth
import streamlit as st
import yaml

def init_auth():
    with open("auth_config_test.yaml") as f:
        config = yaml.safe_load(f)

    auth = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
    )
    return auth

def require_login():
    auth = init_auth()
    name, status, username = auth.login("Login", "main")

    if not status:
        st.stop()  # Bloqueia o resto da página

    return name, username