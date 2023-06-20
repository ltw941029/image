import streamlit as st         
import numpy as np
from PIL import Image

array = np.arange(0, 737280, 1, np.uint8)
array = np.reshape(array, (1024, 720))

im = Image.fromarray(array)
im.save("example4.jpeg")
image = Image.open('example4.jpg')
st.image(image, caption='output_format='auto', width=200, clamp=150, channels='RGB')

