import streamlit as st
from PIL import Image

image = Image.open('example.jpg')

st.image(image, caption='이미지1')

image = Image.open('example1.jpg')

st.image(image, caption='이미지2')

image = Image.open('example2.jpg')

st.image(image, caption='이미지3')

image = Image.open('example.jpg')

st.image(image, caption='width=100', width=100)

image = Image.open('example.jpg')

st.image(image, caption='auto', use_column_width='auto')

image = Image.open('example1.jpg')

st.image(image, caption='always', use_column_width='auto')

image = Image.open('example2.jpg')

st.image(image, caption='never', use_column_width='auto')



