# Importar bibliotecas
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime

data_frame_curva_juros = pd.read_excel('curva_juros.xlsx')

#layout da página central
st.set_page_config(page_title = "Dados de Mercado - Área Macro - Ventor Investimentos", layout = 'centered')
with st.container():
    st.title("Dados de Mercado - Área Macro")
    
# primeiro container - Dados de Juros Nominal
with st.container():
    st.sidebar.image("Logo.png")
    st.sidebar.title("Dados")
    if st.sidebar.checkbox("Curva de Juros Nominal"):
        curva_juros_nominal = px.line(data_frame_curva_juros, x='Data', y='Valor', title='Curva de Juros Nominal')
        st.plotly_chart(curva_juros_nominal)