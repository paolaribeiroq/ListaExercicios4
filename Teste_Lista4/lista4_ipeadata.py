import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import ipeadatapy as ip

st.set_page_config(
    page_title="App Lucas&Paola",
    page_icon="👾",
)

st.header("Lista de Exercícios 4") 
st.subheader("Seja bem-vindo ao Exercício IPEADATA!")

"---"

st.write('Busca na base do IPEADATA os indicadores relacionados a taxa de juros Selic. O objetivo é encontrar o código correspondente ao indicador "Taxa de juros - Over / Selic - acumulada no mês"')

code = '''
ip.list_series('Selic')
'''
st.code(code, language='python')

ip.list_series('Selic')
