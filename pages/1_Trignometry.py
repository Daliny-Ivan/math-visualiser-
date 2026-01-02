# ============ T R I G N O

import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Trigonometry Lab", layout="centered")
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

st.title("📐 Trigonometry Plane")

# ---------- CONTROLS ----------
func = st.selectbox("Choose function", ["sin(x)", "cos(x)", "tan(x)"])

A = st.slider("Amplitude (A)", 0.5, 5.0, 1.0, 0.1)
w = st.slider("Frequency (ω)", 0.5, 5.0, 1.0, 0.1)
phi = st.slider("Phase (φ)", 0.0, 2*np.pi, 0.0, 0.1)

# ---------- DATA ----------
x = np.linspace(-2*np.pi, 2*np.pi, 2000)

if func == "sin(x)":
    y = A * np.sin(w*x + phi)
elif func == "cos(x)":
    y = A * np.cos(w*x + phi)
else:
    y = A * np.tan(w*x + phi)
    y[np.abs(y) > 10] = np.nan  # avoid vertical explosion

# ---------- PLOT ----------
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode="lines",
    line=dict(width=3)
))

# X & Y axes at origin
fig.update_layout(
    template="plotly_dark",
    plot_bgcolor="black",
    paper_bgcolor="black",
    xaxis=dict(
        title="x",
        range=[-2*np.pi, 2*np.pi],
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor="white",
        tickvals=[-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],
        ticktext=["-2π", "-π", "0", "π", "2π"]
    ),
    yaxis=dict(
        title="y",
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor="white",
    ),
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)
