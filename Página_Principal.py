import streamlit as st
from PIL import Image

favicon = Image.open('logo_lific.png')
st.set_page_config(page_title = 'Página Principal', page_icon = favicon)

#Titulo y subir archivos

Col1, Col2, Col3 = st.columns(3)

#if st.theme() == 'light':

Col2.image('https://i.imgur.com/YMei8p1.png', use_column_width='auto')

st.title("Pagina principal de la plataforma")