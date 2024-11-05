import streamlit as st
import pandas as pd
import gspread
from google.oauth2 import service_account
import gspread_dataframe as gd


# Connect to Google Sheets

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ],
)


client = gspread.authorize(credentials=credentials)

Col1, Col2, Col3 = st.columns(3)


Col2.image('https://i.imgur.com/YMei8p1.png',use_column_width='auto')



st.title("Visualizador")

sheet = client.open_by_url(st.secrets["A1modulo1"])

worksheet = sheet.worksheet("Asistencia")

df = pd.DataFrame(worksheet.get("C5:I"))
df.columns = df.iloc[0]
df = df[1:].reset_index(drop=True)
df = df.drop(columns=["Porcentaje Justificadas", "Inasistencias justificadas", "Clases Realizadas"])
df = df[df["Nombre"].notna() & (df["Nombre"].str.strip() != "")]

st.write(df)

st.text("Leer un archivo de GoogleSheet")

st.text("Mostrar un archivo de GoogleSheet")

st.text("Poder escoger archivo")
