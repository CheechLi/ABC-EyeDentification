import streamlit as st

st.set_page_config(
    page_icon="🧿",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("<h1 style='text-align: center;'>About Ocular Disease</h1>", unsafe_allow_html=True)

st.image("images/Four Basic Disease.png", width=700)

st.markdown("### Global impact and diagnostic gaps in ocular diseases")

st.markdown("""
Ocular diseases — a broad term for conditions that affect parts of the eye like the cornea, lens, retina, and optic nerve — affect roughly **2.2 billion people** around the world. Furthermore, almost **two-thirds of adults** report experiencing vision issues, yet only **one in eight** report seeking care.

Although improvements in imaging technology have made it easier to diagnose problems, many people either don’t have access to regular eye care or simply don’t prioritize it. This has caused conditions like **glaucoma**, **cataracts**, and **diabetic retinopathy** to often go unnoticed until they’ve already caused **permanent vision loss**.

As the issue of ocular diseases steadily rises, ophthalmologists are pushing for ways to make diagnosis for these issues as **efficient** and **cheap** as possible.
            
**Learn More**

- https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases
- https://my.clevelandclinic.org/health/diseases/eye-diseases
- https://www.cdc.gov/vision-health/about-eye-disorders/index.html
""")