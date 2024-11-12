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
op_modalidad = st.selectbox("Elegir Modalidad", ["Teórico","Práctico"])

op_asignatura = st.selectbox("Elegir Asignatura", ["A1","A2","A3","A4"])
# st.text(op_asignatura)
   

if op_modalidad == "Teórico":

    match op_asignatura:
        case "A1":
            op_modulo = st.selectbox("Elegir Módulo", ["Todos","1"])
            url_list = [st.secrets["A1modulo1"]]
        case "A2":
            op_modulo = st.selectbox("Elegir Módulo", ["Todos","1","2"])
            url_list = [st.secrets["A2modulo1"],st.secrets["A2modulo2"]]
        case "A3":
            op_modulo = st.selectbox("Elegir Módulo", ["Todos","1"])
            url_list = [st.secrets["A3modulo1"]]
        case "A4":
            op_modulo = st.selectbox("Elegir Módulo", ["Todos","1","X"])
            url_list = [st.secrets["A4modulo1"],st.secrets["A4modulox"]]
    

else: #Práctico
    match op_asignatura:
        case "A1":
            op_modulo = st.selectbox("Elegir Módulo", ["Todos","2","3"])
            url_list = [st.secrets["PA1M02"],st.secrets["PA1M03"]]
        case "A2":
            op_modulo = st.selectbox("Elegir Módulo", ["Todos","4","5","6","7","8","9","10","11","12","13","14","15","17","18","19","20","21","22","23","24"])
            url_list = [st.secrets["PA2M04"],st.secrets["PA1M05"],st.secrets["PA1M06"],st.secrets["PA1M07"],st.secrets["PA1M08"],st.secrets["PA1M09"],st.secrets["PA1M10"],st.secrets["PA1M11"],st.secrets["PA1M12"],st.secrets["PA1M13"],st.secrets["PA1M14"],st.secrets["PA1M15"],st.secrets["PA1M17"],st.secrets["PA1M18"],st.secrets["PA1M19"],st.secrets["PA1M20"],st.secrets["PA1M21"],st.secrets["PA1M22"],st.secrets["PA1M23"],st.secrets["PA1M24"]]
        case "A3":
            op_modulo = st.selectbox("Elegir Módulo", ["Todos","2","3","4","5"])
            url_list = [st.secrets["PA3M02"],st.secrets["PA3M03"],st.secrets["PA3M04"],st.secrets["PA3M05"]]
        case "A4":
            op_modulo = st.selectbox("Elegir Módulo", ["Todos","2","3","4","5","6","7","8","9","10","11","12","X"])
            url_list = [st.secrets["PA4M02"],st.secrets["PA4M03"],st.secrets["PA4M04"],st.secrets["PA4M05"],st.secrets["PA4M06"],st.secrets["PA4M07"],st.secrets["PA4M08"],st.secrets["PA4M09"],st.secrets["PA4M10"],st.secrets["PA4M11"],st.secrets["PA4M12"],st.secrets["PA4Mx"]]

            if op_modulo == 'Todos':
                for i in range(url_list):
                    


st.text("Modalidad: {}, Asignatura: {}, Modulo: {}".format(op_modalidad,op_asignatura,op_modulo))

st.text("url_list: {}".format(url_list))
sheet = client.open_by_url(st.secrets["A1modulo1"])

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
