# login.py
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="centered")

# 🔐 Listen for auth result
auth_data = st.experimental_get_query_params()

st.markdown("## 🔐 ScreenerPro Login")

components.html(
    open("login.html", "r", encoding="utf-8").read(),
    height=720,
    scrolling=False,
)
