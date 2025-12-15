import streamlit as st
import streamlit.components.v1 as components
import requests

from firebase_config import FIREBASE_AUTH_SIGNIN_URL

# ======================================================
# LOGIN SECTION (HTML BASED)
# ======================================================
def login_section():

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    st.markdown("<style>header{visibility:hidden;}</style>", unsafe_allow_html=True)

    # Load HTML
    with open("auth/login.html", "r", encoding="utf-8") as f:
        html = f.read()

    data = components.html(html, height=650)

    # 🚀 DATA COMING FROM HTML
    if data and data.get("action") == "login":
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            st.error("Email and password required")
            return False

        # Firebase auth
        auth_res = requests.post(
            FIREBASE_AUTH_SIGNIN_URL,
            json={"email": email, "password": password, "returnSecureToken": True},
        )

        if auth_res.status_code != 200:
            st.error("❌ Invalid credentials")
            return False

        auth = auth_res.json()
        st.session_state.authenticated = True
        st.session_state.user_uid = auth["localId"]
        st.session_state.user_email = email

        st.rerun()
