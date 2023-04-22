import streamlit as st
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    from PIL import Image
    image = Image.open(uploaded_file)

    st.image(image, caption='uploaded image')
    