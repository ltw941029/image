import streamlit as st         
import numpy as np
from PIL import Image

array = np.arange(0, 737280, 1, np.uint8)
array = np.reshape(array, (1024, 720))

im = Image.fromarray(array)
st.image(im, caption='output_format='auto', width=200, clamp=150, channels='RGB')
