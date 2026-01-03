import streamlit as st
import numpy as np
import plotly.graph_objects as go
import os, base64
#-----BG-----------
'''
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
'''
#------MAIN PG LOGIC--------

st.set_page_config(page_title="Logarithms", layout="centered")

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

st.title("📊 Logarithmic Analysis")

base = st.slider("Log base", 2.0, 10.0, 10.0)
scale = st.slider("Scale factor", 0.5, 5.0, 1.0)

x = np.linspace(0.01, 10, 1000)
y = scale * np.log(x) / np.log(base)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode="lines", line=dict(width=3)))

fig.update_layout(
    title=f"y = {scale} log₍{base}₎(x)",
    template="plotly_dark",
    xaxis=dict(zeroline=True),
    yaxis=dict(zeroline=True),
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)
