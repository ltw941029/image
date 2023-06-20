import streamlit as st         
import numpy as np
from PIL import Image

img = Image.open("example.jpg")
imgArray = np.asarray(img)
st.image(imagArray, caption='output_format=auto', width=200)

