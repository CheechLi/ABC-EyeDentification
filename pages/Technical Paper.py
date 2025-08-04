import streamlit as st

st.set_page_config(
    page_icon="🧿",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("Download Technical Paper")

pdf_path = "Eye-Dentification Tehnical Paper.pdf"

with open(pdf_path, "rb") as f:
    pdf_bytes = f.read()

st.download_button(
    label="Click to Download Technical Paper",
    data=pdf_bytes,
    file_name="Eye-Dentification Tehnical Paper.pdf",
    mime="application/pdf"
)
