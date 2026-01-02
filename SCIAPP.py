#       S C I    A P P

import streamlit as st

st.set_page_config(page_title="Science App", layout="centered")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e0e0e;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("SCIENCE APP")
st.subheader("Choose from below!!")

st.write("""
Explore interactive graphs:
- Trigonometry
- Algebra
- Logarithms
- Conic
""")

st.info("Use the sidebar to navigate")
