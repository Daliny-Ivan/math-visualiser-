# ========= A L G E B R A   L A B

import streamlit as st
import numpy as np
import plotly.graph_objects as go

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

# ------MAIN 
st.set_page_config(page_title="Algebra Lab", layout="centered")

# ----- Dark theme -----
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

st.title("🧮 Algebra Lab")
st.caption("Pure algebraic functions ")

# ----- Graph selector -----
graph_type = st.selectbox(
    "Choose equation type",
    [
        "Linear",
        "Quadratic (Standard)",
        "Quadratic (Vertex Form)",
        "Polynomial (Degree n)",
        "Power Function"
    ]
)

x = np.linspace(-10, 10, 3000)

# ----- LOGIC -----
if graph_type == "Linear":
    st.markdown("### y = mx + c")
    m = st.slider("m (slope)", -100.0, 100.0, 1.0)
    c = st.slider("c (intercept)", -100.0, 100.0, 0.0)
    y = m * x + c
    title = "Linear Function"

elif graph_type == "Quadratic (Standard)":
    st.markdown("### y = ax² + bx + c")
    a = st.slider("a", -100.0, 100.0, 1.0)
    b = st.slider("b", -100.0, 100.0, 0.0)
    c = st.slider("c", -100.0, 100.0, 0.0)
    y = a * x**2 + b * x + c
    title = "Quadratic (Standard Form)"

elif graph_type == "Quadratic (Vertex Form)":
    st.markdown("### y = a(x − h)² + k")
    a = st.slider("a", -100.0, 100.0, 1.0)
    h = st.slider("h (shift)", -10.0, 10.0, 0.0)
    k = st.slider("k (shift)", -100.0, 100.0, 0.0)
    y = a * (x - h)**2 + k
    title = "Quadratic (Vertex Form)"

elif graph_type == "Polynomial (Degree n)":
    st.markdown("### y = aₙxⁿ + ... + a₁x + a₀")
    degree = st.slider("Degree (n)", 1, 6, 3)
    coeffs = []
    for i in range(degree + 1):
        coeffs.append(
            st.slider(f"Coefficient a{i}", -50.0, 50.0, 1.0)
        )

    y = np.zeros_like(x)
    for i, coef in enumerate(coeffs):
        y += coef * x**(degree - i)

    title = f"Polynomial Degree {degree}"

else:  # Power function
    st.markdown("### y = axⁿ")
    a = st.slider("a", -50.0, 50.0, 1.0)
    n = st.slider("n (power)", -5.0, 5.0, 2.0)
    y = a * np.power(np.abs(x), n)
    title = "Power Function"

# ----- PLOT -----
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=x,
        y=y,
        mode="lines",
        line=dict(width=3, color="cyan")
    )
)

fig.update_layout(
    title=title,
    template="plotly_dark",
    xaxis=dict(
        zeroline=True,
        zerolinewidth=2,
        gridcolor="rgba(255,255,255,0.1)"
    ),
    yaxis=dict(
        zeroline=True,
        zerolinewidth=2,
        gridcolor="rgba(255,255,255,0.1)"
    ),
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)
