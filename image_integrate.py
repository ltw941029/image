import streamlit as st
from PIL import Image

image = Image.open('example.jpg')

st.image(image, caption='image1')

image1 = Image.open('example1.jpg')

st.image(image1, caption='image2')

image2 = Image.open('example2.jpg')

st.image(image2, caption='image3')

image3 = Image.open('example.jpg')

st.image(image3, caption='width=100', width=100)

image4 = Image.open('example1.jpg')

st.image(image4, caption='auto', use_column_width='auto')

image5 = Image.open('example2.jpg')

st.image(image5, caption='always',use_column_width='always')

image6 = Image.open('example.jpg')

st.image(image6, caption='never',use_column_width='never')

image7 = Image.open('example1.jpg')

st.image(image7, caption='width & use_column_width',width='10', use_column_width='always')

import streamlit as st
from PIL import Image

image8 = Image.open('example.jpg')

st.image(image8, caption='clamp=True', width=200, clamp=True)
