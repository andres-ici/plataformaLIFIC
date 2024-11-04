import streamlit as st



Col1, Col2, Col3 = st.columns(3)


Col2.image('https://i.imgur.com/YMei8p1.png',use_column_width='auto')


st.title("Visualizador")

st.text("Leer un archivo de GoogleSheet")

st.text("Mostrar un archivo de GoogleSheet")

st.text("Poder escoger archivo")
