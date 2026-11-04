#Execução: python -m streamlit run frontend.py

import streamlit as st
from open_meteo import obter_dados_meteorologicos

st.set_page_config(page_title="Dados Meteorológicos", page_icon="🌤️")

st.title("Dados Meteorológicos")
st.caption("Monitoramento de condições atuais")

try:
    dados = obter_dados_meteorologicos()

    temperatura = dados["temperatura"]
    umidade = dados["umidade_relativa"]
    sensacao = dados["sensacao_termica"]
    precipitacao = dados["precipitacao"]
    vento = dados["velocidade_vento"]
    horario = dados["horario"]

    st.metric("Temperatura do ar", f"{temperatura:.1f} °C")
    st.metric("Umidade relativa", f"{umidade:.0f} %")
    st.metric("Sensação térmica", f"{sensacao:.1f} °C")
    st.metric("Precipitação", f"{precipitacao:.1f} mm")
    st.metric("Velocidade do vento", f"{vento:.1f} km/h")

    st.write(f"Horário informado pela API: {horario}")

except Exception as erro:
    st.error(f"Não foi possível apresentar os dados: {erro}")