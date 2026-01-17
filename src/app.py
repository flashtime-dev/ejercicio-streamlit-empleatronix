import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Empleatronix')
st.text('Todos los datos sobre los empleados en una aplicación.')

data = pd.read_csv('data/employees.csv')
st.dataframe(data)
st.markdown('---')

col1, col2, col3 = st.columns(3)
color = col1.color_picker('Elige un color para resaltar', "#3470B4")
mostrar_nombre = col2.toggle('Mostrar el nombre', value=True)
mostrar_sueldo = col3.toggle('Mostrar sueldo en la barra')

fig, ax = plt.subplots(figsize=(8, 6))

# Grafica de barras horizontales
bars = ax.barh(
    data['full name'],
    data['salary'],
    color=color
)

# Mostrar/ocultar sueldo al final de cada barra
if mostrar_sueldo:
    ax.bar_label(bars, fmt="%.0f€", padding=3)


# Mostrar/ocultar nombres
if not mostrar_nombre:
    ax.set_yticks([])

# Eje X
ax.set_xticks(range(0, 4501, 500))
plt.xticks(rotation=90)

# Mostrar en Streamlit
st.pyplot(fig)


st.write("© Cristina Vacas López - CPIFP Alan Turing")