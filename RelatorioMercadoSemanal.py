# Importar bibliotecas
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime

curva_de_juros_di = pd.read_excel('curva_juros.xlsx', sheet_name= 'DI1')
curva_de_juros_dap = pd.read_excel('curva_juros.xlsx', sheet_name= 'DAP')

#layout da página central
st.set_page_config(page_title = "Dados de Mercado - Área Macro - Ventor Investimentos", layout = 'centered')
with st.container():
    st.title("Dados de Mercado - Área Macro")
    
# primeiro container - Dados de Juros Nominal
with st.container():
    st.sidebar.image("Logo.png")
    st.sidebar.title("Dados")
    if st.sidebar.checkbox("Curva de Juros Nominal"):
        curva_juros_nominal = px.line(
            curva_de_juros_di,
            x='Data',
            y='Valor',
            title='Curva de Juros Nominal',
            markers=True
        )
        curva_juros_nominal.update_traces(line=dict(color='#4BACC6'))
        curva_juros_nominal.update_layout(
            xaxis=dict(showgrid=True, gridcolor='#F2F2F2'),
            yaxis=dict(showgrid=True, gridcolor='#F2F2F2'),
        )
        st.plotly_chart(curva_juros_nominal)
        
    if st.sidebar.checkbox("Curva de Juros Real"):
        curva_juros_real = px.line(
            curva_de_juros_dap,
            x='Data',
            y='Valor',
            title='Curva de Juros Real',
            markers=True
        )
        curva_juros_real.update_traces(line=dict(color='#A50021'))
        curva_juros_real.update_layout(
            xaxis=dict(showgrid=True, gridcolor='#F2F2F2'),
            yaxis=dict(showgrid=True, gridcolor='#F2F2F2'),
        )
        st.plotly_chart(curva_juros_real)
