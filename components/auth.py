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
    auth.login(location="main")
    if not st.session_state.get("authentication_status"):
        st.warning("Por favor, faça login.")
        st.stop()

    return (
        st.session_state.get("name"),
        st.session_state.get("username")
    )