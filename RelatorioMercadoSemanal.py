# Importar bibliotecas
from util.LagunaAPI import getAPIanonimo
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime

#layout da página central
st.set_page_config(page_title = "Dados de Mercado - Área Macro - Ventor Investimentos", layout = 'centered')
with st.container():
    st.title("Dados de Mercado - Área Macro")

dicionário_de_curvas = {
    'M25': datetime(2025, 6, 2),
    'N25': datetime(2025, 7, 1),
    'Q25': datetime(2025, 8, 1),
    'U25': datetime(2025, 9, 1),
    'V25': datetime(2025, 10, 1),
    'X25': datetime(2025, 11, 3),
    'F26': datetime(2026, 1, 2),
    'J26': datetime(2026, 4, 1),
    'N26': datetime(2026, 7, 1),
    'V26': datetime(2026, 10, 1),
    'F27': datetime(2027, 1, 4),
    'J27': datetime(2027, 4, 1),
    'N27': datetime(2027, 7, 1),
    'F28': datetime(2028, 1, 4),
    'F29': datetime(2029, 1, 4),
    'F30': datetime(2030, 1, 4),
    'F31': datetime(2031, 1, 4),
    'F32': datetime(2032, 1, 4),
    'F33': datetime(2033, 1, 4),
    'F34': datetime(2034, 1, 4),
    'F35': datetime(2035, 1, 4)
}

valores_curva_de_juros = []

for ativo, data_vencimento in dicionário_de_curvas.items():
    valor = getAPIanonimo('DadoAtivo', 'get', 'ativo', 'DI1' + ativo, 'data', '5/30/2025', 'dado', 'TaxaAjuste')
    valores_curva_de_juros.append({'Data': data_vencimento,
                                'Ativo': ativo,
                                'Valor': valor})

data_frame_curva_juros = pd.DataFrame(valores_curva_de_juros)
data_frame_curva_juros['Valor'] = pd.to_numeric(data_frame_curva_juros['Valor'],
                                                errors='coerce')

# primeiro container - Dados de Juros Nominal
with st.container():
    st.sidebar.image("Logo.png")
    st.sidebar.title("Dados")
    if st.sidebar.checkbox("Curva de Juros Nominal"):
        curva_juros_nominal = px.line(data_frame_curva_juros, x='Data', y='Valor', title='Curva de Juros Nominal')
        st.plotly_chart(curva_juros_nominal)