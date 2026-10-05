import streamlit as st
import pandas as pd
import plotly.graph_objects as go
df = pd.read_csv('vehicles_us.csv')
st.header('¿Qué happ pasado con mis anuncios?')
boton_hist = st.button('Hacer un histograma')

if boton_hist:
    st.write('Crear el histograma para los datos de anuncios de ventas de autos')
    grafica = go.Figure(data=[go.Histogram(x=df['price'])])
    grafica.update_layout(title_text='Distribución del precio')
    st.plotly_chart(grafica, use_container_width=True)

boton_dispersion = st.button('Genera una gráfica de dispersión')
if boton_dispersion:
    st.write('Elabora una gráfica de dispersión')
    graf = go.Figure(data= [go.Scatter (x=df['odometer'], y=df['price'], mode='markers')])
    graf.update_layout(title_text='Relación entre el odómetro y el precio')
    st.plotly_chart(graf, use_container_width=True)