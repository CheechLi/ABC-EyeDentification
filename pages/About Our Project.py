import streamlit as st

st.markdown("<h1 style='text-align: center;'>About Our Project</h1>", unsafe_allow_html=True)

st.markdown("""
ABC Eye-Dentification uses deep learning to classify eye images into four categories:
            
- **Cataract**
- **Diabetic Retinopathy**
- **Glaucoma**
- **Normal**
            
We aim to raise awareness about the prevalence of ocular diseases and the importance of early detection.
Our goal is to create a smart classifier that can help detect common ocular diseases early and provide a platform for students and researchers to explore medical AI hands-on.
We invite volunteers to upload ocular images to help us diversify our dataset and improve model performance.
""")

st.markdown("""
### What We Did
- Built and trained a CNN using InceptionV3, EfficientNetB5, and DenseNet201 architectures
- Achieved ~91% validation accuracy
- Deployed a real-time web app for public use
""")