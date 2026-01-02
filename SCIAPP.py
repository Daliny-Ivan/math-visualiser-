#       S C I    A P P

import streamlit as st
import os
import base64
#-----BG-----------

sd=os.path.dirname(os.path.abspath(__file__))
bg_p=os.path.join(sd,"assests","bg_sciapp.png")

if not os.path.exists(bg_p):
    bg_p=os.path.join(sd,"assets","bg_sciapp.png")
with open(bg_p,"rb") as f:
    encoded= base64.b64encode(f.read()).decode()

st.markdown(f"""
<style>
.stApp {{
background-image: url("data:image/png;base64,{encoded}");
background-size:cover;
background-position:center;
background-repeat: no-repeat;
background-attachment:fixed;
}}

.block-container {{
background-colour:rgba(0,0,0,0.55);
padding: 2rem;
border-radius:15px;
}}
h1,h2,h3,p,label{{
colour:white !important;
}}
</style>
""",unsafe_allow_html=True)
#-----------Config log--
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


st.title("M*ATH* V*ISUALISER*")
st.subheader("Select from Below!")

st.write("""
Explore interactive graphs:
- Trigonometry
- Algebra
- Logarithms
- Conic
""")

st.write("Visual and interactive graphs helps student understand the following mathematical concepts better.")
st.info("Use the sidebar to navigate")
