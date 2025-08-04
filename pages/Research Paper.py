import streamlit as st
import base64

st.set_page_config(
    page_icon="🧿",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("<h1 style='text-align: center;'>Research Paper</h1>", unsafe_allow_html=True)

pdf_path = "Eye-Dentification Tehnical Paper.pdf"

with open(pdf_path, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode("utf-8")

pdf_display = f"""
    <iframe
        src="data:application/pdf;base64,{base64_pdf}"
        width="700"
        height="1000"
        type="application/pdf"
    ></iframe>
"""

st.markdown(pdf_display, unsafe_allow_html=True)