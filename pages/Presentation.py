import streamlit as st

st.set_page_config(
    page_icon="🧿",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("<h1 style='text-align: center;'>In-Depth Video Presentation</h1>", unsafe_allow_html=True)

youtube_url = "https://youtu.be/z2hk7lZia24"  # Replace with your YouTube video URL
st.video(youtube_url)

st.markdown("""
Voices Credits:
1. Yingqi (Cheech) Li
2. Aaditya Penmetsa
3. Brigitta Yu
4. Aaditya Penmetsa, Brigitta Yu, Yingqi (Cheech) Li
5. Yingqi (Cheech) Li
6. Aaditya Penmetsa, Brigitta Yu
7. Yingqi (Cheech) Li

""")