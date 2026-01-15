import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title('Empleatronix')
st.text('Todos los datos sobre los empleados en una aplicación.')

data = pd.read_csv('data/employees.csv')
st.dataframe(data)
st.markdown('---')

col1, col2, col3 = st.columns(3)
color = col1.color_picker('Elige un color para resaltar', "#3470B4")
mostrar_nombre = col2.toggle('Mostrar el nombre', value=True)
mostrar_sueldo = col3.toggle('Mostrar sueldo en la barra')

fig = go.Figure()

# Barra horizontal
fig.add_trace(go.Bar(
    y=data['full name'],
    x=data['salary'],
    marker_color=color,
    orientation='h',
    text=[f"{s}€" for s in data['salary']] if mostrar_sueldo else [],
    textfont=dict(
        size=16,
        color='black'
    ),
    textposition='outside',
))

# Actualizar el diseño del gráfico
fig.update_layout(
    yaxis=dict(
        tickvals=[] if not mostrar_nombre else None,
        tickfont=dict(color="black", size=16),
        tickcolor="black",
    ),
    xaxis=dict(
        range=[0, 4500],
        dtick=500,
        tickangle=270,
        tickformat=",d €",
        tickfont=dict(color="black", size=16),
        tickcolor="black",  
    ),
    margin=dict(l=50, r=20, t=20, b=50),  # margenes para que 4500 no se corte
    template='simple_white',
)

# Mostrar gráfico fijo
st.plotly_chart(fig, config={"staticPlot": True,})

st.write("© Cristina Vacas López - CPIFP Alan Turing")