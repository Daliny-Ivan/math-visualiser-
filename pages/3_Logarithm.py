#       ----------log
import streamlit as st
import numpy as np
import plotly.graph_objects as go

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
