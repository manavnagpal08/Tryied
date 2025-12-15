import streamlit.components.v1 as components

components.html(
    open("login.html", encoding="utf-8").read(),
    height=900,
    scrolling=False
)
