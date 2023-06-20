import streamlit as st
from PIL import Image

st.image((10,10,1),caption='단색 이미지')
st.image((10,10,3),caption='컬러 이미지')
st.image((10,10,4),caption='RGBA 이미지')


image = Image.open('example.jpg')

st.image(image, caption='로컬 이미지')
