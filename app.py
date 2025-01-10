import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_mandelbrot(h, w, max_iter):
    y, x = np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j]
    c = x + y*1j
    z = c
    divtime = max_iter + np.zeros(z.shape, dtype=int)

    for i in range(max_iter):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime == max_iter)
        divtime[div_now] = i
        z[diverge] = 2

    return divtime

st.set_page_config(layout="wide")
st.title("Fractal Explorer")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Controls")
    resolution = st.slider("Resolution", 100, 1000, 500, step=100)
    iterations = st.slider("Iterations", 20, 100, 50)
    colormap = st.selectbox(
        "Color Scheme",
        ["magma", "viridis", "plasma", "inferno", "cividis"]
    )

with col2:
    st.subheader("Mandelbrot Set")
    
    fig, ax = plt.subplots(figsize=(10, 10), facecolor='#1B1C20')
    ax.set_facecolor('#1B1C20')
    
    mandelbrot = generate_mandelbrot(resolution, resolution, iterations)
    img = ax.imshow(mandelbrot, cmap=colormap)
    plt.colorbar(img)
    
    # Customize the plot
    ax.set_title("Mandelbrot Set Visualization", color='white', pad=20)
    ax.set_xticks([])
    ax.set_yticks([])
    
    st.pyplot(fig)

st.markdown("""
### About this Fractal Explorer
This app visualizes the Mandelbrot set, one of the most famous fractals in mathematics. 
The colors represent how quickly each point escapes the set during iteration.

- Use the resolution slider to adjust the detail level
- Increase iterations for more precise boundaries
- Try different color schemes to explore the pattern
""")