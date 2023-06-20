import streamlit as st
from PIL import Image
import numpy as np

a=np.array([10,10,1])
st.image(a,caption='단색 이미지')
st.image((10,10,3),caption='컬러 이미지')
st.image((10,10,4),caption='RGBA 이미지')


image = Image.open('example.jpg')

st.image(image, caption='로컬 이미지')
