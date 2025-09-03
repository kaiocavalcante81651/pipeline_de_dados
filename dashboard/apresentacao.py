import streamlit as st
import pandas as pd
from database.db import temperaturas, retorna_dados

def exibir():
    st.title("Dashboard de Temperaturas IoT")

    menu = st.sidebar.selectbox(
        "Escolha uma opção",
        ["Tabelas", "Gráficos"]
    )

    if menu == "Tabelas":
        st.subheader("Tabelas")
        st.write("Temperaturas por dispositivo")
        #temp = temperaturas()
        #dados = retorna_dados()
        dados = temperaturas()
        st.dataframe(dados)