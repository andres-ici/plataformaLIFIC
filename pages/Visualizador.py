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

sheet = client.open_by_url(st.secrets["A4modulo1"])

worksheet = sheet.worksheet("Asistencia")

df = pd.DataFrame(worksheet.get("C5:I"))
df.columns = df.iloc[0]
df = df[1:].reset_index(drop=True)
df = df.drop(columns=["Porcentaje Justificadas", "Inasistencias justificadas", "Clases Realizadas"])
df = df[df["Nombre"].notna() & (df["Nombre"].str.strip() != "")]
df['Modalidad'] = 'Teórico'
df['Módulo'] = 1
df = df[['Nombre','Matrícula', 'Modalidad', 'Módulo', 'Porcentaje Asistencia', 'Inasistencias no justificadas']]

st.write(df)

sheet2 = client.open_by_url(st.secrets["PA4M02"])

worksheet2 = sheet2.worksheet("Asistencia")

df2 = pd.DataFrame(worksheet2.get("C5:I"))
df2.columns = df2.iloc[0]
df2 = df2[1:].reset_index(drop=True)
df2 = df2.drop(columns=["Porcentaje Justificadas", "Inasistencias justificadas", "Clases Realizadas"])
df2 = df2[df2["Nombre"].notna() & (df2["Nombre"].str.strip() != "")]
df2['Modalidad'] = 'Práctico'
df2['Módulo'] = 2
df2 = df2[['Nombre','Matrícula', 'Modalidad', 'Módulo', 'Porcentaje Asistencia', 'Inasistencias no justificadas']]

st.write(df2)

df_combined = pd.concat([df, df2], ignore_index=False)

st.write(df_combined)

st.text("Leer un archivo de GoogleSheet")

st.text("Mostrar un archivo de GoogleSheet")

st.text("Poder escoger archivo")
