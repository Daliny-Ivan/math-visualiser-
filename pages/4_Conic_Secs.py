# -------C O N I C

import streamlit as st
import numpy as np
import plotly.graph_objects as go
#----end---
'''
# Dark background
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

st.title("🌀 Conic Sections Lab")

conic = st.selectbox(
    "Choose a conic section",
    ["Circle", "Parabola", "Ellipse", "Hyperbola"]
)

x = np.linspace(-100, 100, 1000)

fig = go.Figure()

# ───────── CIRCLE ─────────
if conic == "Circle":
    r = st.slider("Radius (r)", 1, 100, 10)
    theta = np.linspace(0, 2*np.pi, 1000)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines"))
    fig.update_layout(template='plotly_dark',
                      xaxis=dict(
                          zeroline=True,
                          zerolinewidth=2,
                          scaleanchor='y',
                          scaleratio=1),
                      yaxis=dict(
                          zeroline=True,
                          zerolinewidth=2),
                      showlegend=False)

# ───────── PARABOLA ─────────
elif conic == "Parabola":
    a = st.slider("Coefficient (a)", -10.0, 10.0, 1.0)
    y = a * x**2
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines"))

# ───────── ELLIPSE ─────────
elif conic == "Ellipse":
    a = st.slider("Semi-major axis (a)", 1, 100, 20)
    b = st.slider("Semi-minor axis (b)", 1, 100, 10)
    theta = np.linspace(0, 2*np.pi, 1000)
    x = a * np.cos(theta)
    y = b * np.sin(theta)
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines"))

# ───────── HYPERBOLA ─────────
elif conic == "Hyperbola":
    a = st.slider("a", 1, 50, 10)
    b = st.slider("b", 1, 50, 5)
    y = np.sqrt((x**2 / a**2 - 1)) * b
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines"))
    fig.add_trace(go.Scatter(x=x, y=-y, mode="lines"))

# ───────── GRAPH STYLE ─────────
fig.update_layout(
    paper_bgcolor="#0e0e0e",
    plot_bgcolor="#0e0e0e",
    font_color="white",
    xaxis=dict(
        title="X-axis",
        zeroline=True,
        zerolinecolor="gray",
        gridcolor="#333"
    ),
    yaxis=dict(
        title="Y-axis",
        zeroline=True,
        zerolinecolor="gray",
        gridcolor="#333"
    ),
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)
