import streamlit as st
import pandas as pd
import plotly.express as px
from database.db import temperaturas, retorna_dados, data_temperatura

def exibir():
    st.title("Dashboard de Temperaturas IoT")

    menu = st.sidebar.selectbox(
        "Escolha uma opção",
        ["Tabelas", "Gráficos"]
    )

    if menu == "Tabelas":
        st.write("Temperaturas por dispositivo")
        dados = temperaturas()
        st.dataframe(dados)

    elif menu == "Gráficos":
        st.subheader("Gráficos")
        df = data_temperatura()
        fig = px.line(
            df,
            x="data",
            y="temp",
            title="Gráfico de temperatura por data",
            labels={"data": "Data", "temp":"Temperatura média (°C)"},
            markers=True
        )
        st.plotly_chart(fig)