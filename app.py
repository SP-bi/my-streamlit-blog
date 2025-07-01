import streamlit as st

st.set_page_config(page_title="My Blog", layout="wide")
st.title("📘 My Blog Embedded")

st.markdown("(https://power-bi-dev.blogspot.com/)")

st.components.v1.iframe("https://power-bi-dev.blogspot.com/", height=1000)
