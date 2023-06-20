import streamlit as st
from PIL import Image

image8 = Image.open('example.jpg')

st.image(image8, caption='output_format='auto', width=200, clamp=150, channels='RGB')
