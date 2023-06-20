import streamlit as st
from PIL import Image

image = Image.open('example.jpg')

st.image(image, caption='이미지1')




