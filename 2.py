import streamlit as st
from PIL import Image

image8 = Image.open('example.jpg')

st.image(image8, caption='clamp=150', width=200, clamp=150)



