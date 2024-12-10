import streamlit as st
import pandas as pd
import gspread
from google.oauth2 import service_account
import gspread_dataframe as gd
import re

def generarDF(url_list2):

    dfFinal = pd.DataFrame(columns=['Nombre','Matrícula', 'Modalidad', 'Módulo', 'Porcentaje Asistencia', 'Inasistencias no justificadas'])

    for i in range(len(url_list2)):

        sheet = client.open_by_url(st.secrets[url_list2[i]])

        worksheet = sheet.worksheet("Asistencia")

        df = pd.DataFrame(worksheet.get("C5:I"))
        df.columns = df.iloc[0]
        df = df[1:].reset_index(drop=True)
        df = df.drop(columns=["Porcentaje Justificadas", "Inasistencias justificadas", "Clases Realizadas"])
        df = df[df["Nombre"].notna() & (df["Nombre"].str.strip() != "")]
        df['Modalidad'] = 'Teórico'
        
        try:
            df['Módulo'] = int(str(url_list2[i][-2:]))
        except:
            df['Módulo'] = 'x'
            
        df = df[['Nombre','Matrícula', 'Modalidad', 'Módulo', 'Porcentaje Asistencia', 'Inasistencias no justificadas']]
        df['Porcentaje Asistencia'] = df['Porcentaje Asistencia'].str.replace('%', '').astype(int)

        dfFinal = df_combined = pd.concat([df, dfFinal], ignore_index=False)
        
    print(dfFinal)
    return dfFinal



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


Col2.image('https://i.imgur.com/YMei8p1.png',use_container_width ='auto')



st.title("Visualizador")

sheet = client.open_by_url(st.secrets["A4modulo1"])
op_modalidad = st.selectbox("Elegir Modalidad", ["Teórico","Práctico"])

op_asignatura = st.selectbox("Elegir Asignatura", ["A1","A2","A3","A4"])
# st.text(op_asignatura)

if st.botton("Gener tablas"):

    if op_modalidad == "Teórico":

        match op_asignatura:
            case "A1":
                op_modulo = st.selectbox("Elegir Módulo", ["Todos","1"])
                url_list2 = ["TA1M01"]
                st.text("Modalidad: {}, Asignatura: {}, Modulo: {}".format(op_modalidad,op_asignatura,op_modulo))
                df = generarDF(url_list2)

                if op_modulo == "Todos":
                    st.write(df)
                else:
                    try:
                        st.write(df[df["Módulo"] == int(op_modulo)])
                    except:
                        st.write(df[df["Módulo"] == op_modulo])
                        
            case "A2":
                op_modulo = st.selectbox("Elegir Módulo", ["Todos","1","2"])
                url_list2 = ["TA2M01", "TA2M02"]
                st.text("Modalidad: {}, Asignatura: {}, Modulo: {}".format(op_modalidad,op_asignatura,op_modulo))
                df = generarDF(url_list2)

                if op_modulo == "Todos":
                    st.write(df)
                else:
                    try:
                        st.write(df[df["Módulo"] == int(op_modulo)])
                    except:
                        st.write(df[df["Módulo"] == op_modulo])
                        
            case "A3":
                op_modulo = st.selectbox("Elegir Módulo", ["Todos","1"])
                url_list2 = ["TA3M01"]
                st.text("Modalidad: {}, Asignatura: {}, Modulo: {}".format(op_modalidad,op_asignatura,op_modulo))
                df = generarDF(url_list2)

                if op_modulo == "Todos":
                    st.write(df)
                else:
                    try:
                        st.write(df[df["Módulo"] == int(op_modulo)])
                    except:
                        st.write(df[df["Módulo"] == op_modulo])
                        
            case "A4":
                op_modulo = st.selectbox("Elegir Módulo", ["Todos","01"])
                url_list2 = ["TA4M01"]
                st.text("Modalidad: {}, Asignatura: {}, Modulo: {}".format(op_modalidad,op_asignatura,op_modulo))
                df = generarDF(url_list2)

                if op_modulo == "Todos":
                    st.write(df)
                else:
                    try:
                        st.write(df[df["Módulo"] == int(op_modulo)])
                    except:
                        st.write(df[df["Módulo"] == op_modulo])

        

    else: #Práctico
        match op_asignatura:
            case "A1":
                op_modulo = st.selectbox("Elegir Módulo", ["Todos","2","3"])
                url_list = [st.secrets["PA1M02"],st.secrets["PA1M03"]]
                
                url_list2 = ["PA1M02", "PA1M03"]
                
                st.text("Modalidad: {}, Asignatura: {}, Modulo: {}".format(op_modalidad,op_asignatura,op_modulo))

                df = generarDF(url_list2)

                if op_modulo == "Todos":
                    st.write(df)
                else:
                    try:
                        st.write(df[df["Módulo"] == int(op_modulo)])
                    except:
                        st.write(df[df["Módulo"] == op_modulo])
                        
            case "A2":
                op_modulo = st.selectbox("Elegir Módulo", ["Todos","4","5","6","7","8","9","10","11","12","13","14","15","17","18","19","20","21","22","23","24"])
                
                url_list2 = ["PA2M04", "PA2M05", "PA2M06", "PA2M07", "PA2M08", "PA2M09", "PA2M10", "PA2M11", "PA2M12", "PA2M13", "PA2M14", "PA2M15", "PA2M15", "PA2M17", "PA2M18", "PA2M19", "PA2M20", "PA2M21", "PA2M22", "PA2M23", "PA2M24"]
                
                st.text("Modalidad: {}, Asignatura: {}, Modulo: {}".format(op_modalidad,op_asignatura,op_modulo))

                df = generarDF(url_list2)

                if op_modulo == "Todos":
                    st.write(df)
                else:
                    try:
                        st.write(df[df["Módulo"] == int(op_modulo)])
                    except:
                        st.write(df[df["Módulo"] == op_modulo])
                
            case "A3":
                op_modulo = st.selectbox("Elegir Módulo", ["Todos","2","3","4","5"])
                
                url_list2 = ["PA3M02", "PA3M03", "PA3M04", "PA3M05"]
                
                st.text("Modalidad: {}, Asignatura: {}, Modulo: {}".format(op_modalidad,op_asignatura,op_modulo))

                df = generarDF(url_list2)

                if op_modulo == "Todos":
                    st.write(df)
                else:
                    try:
                        st.write(df[df["Módulo"] == int(op_modulo)])
                    except:
                        st.write(df[df["Módulo"] == op_modulo])
                        
            case "A4":
                op_modulo = st.selectbox("Elegir Módulo", ["Todos","2","3","4","5","6","7","8","9","10","11","12","x"])

                url_list2 = ["PA4M02", "PA4M03", "PA4M04", "PA4M05", "PA4M06", "PA4M07", "PA4M08", "PA4M09", "PA4M10", "PA4M11", "PA4M12", "PA4M0x"]
                
                st.text("Modalidad: {}, Asignatura: {}, Modulo: {}".format(op_modalidad,op_asignatura,op_modulo))

                df = generarDF(url_list2)

                if op_modulo == "Todos":
                    st.write(df)
                else:
                    try:
                        st.write(df[df["Módulo"] == int(op_modulo)])
                    except:
                        st.write(df[df["Módulo"] == op_modulo])

                        

