# Empleatronix 📊

Una aplicación web interactiva para visualizar y analizar datos de empleados construida con **Streamlit** y **Plotly**.

## 🎯 Descripción

**Empleatronix** es una herramienta intuitiva diseñada para presentar información de empleados de forma clara y atractiva. La aplicación permite customizar la visualización de datos mediante controles interactivos, facilitando el análisis rápido de información salarial.

## ✨ Características

- 📋 **Vista de tabla interactiva**: Carga y visualiza datos de empleados desde CSV
- 🎨 **Selector de color personalizado**: Elige el color de las barras del gráfico
- 👤 **Toggle de visibilidad**: Muestra u oculta los nombres de los empleados
- 💰 **Toggle de etiquetas de sueldo**: Muestra u oculta los valores salariales en el gráfico
- 📊 **Gráfico de barras horizontal**: Visualización clara de salarios con Plotly

## 🛠️ Requisitos

- Python 3.8+
- pandas
- streamlit
- plotly

## 📦 Instalación

1. Construye la imagen Docker:
```bash
docker-compose build
```

2. Ejecuta el contenedor:
```bash
docker-compose up
```


La aplicación se abrirá en `http://localhost:8501`


## 🎮 Instrucciones de Uso

1. **Elige un color**: Usa el selector de color para personalizar el color de las barras.
2. **Mostrar/Ocultar nombres**: Usa el toggle "Mostrar el nombre" para controlar la visualización de nombres en el eje Y.
3. **Mostrar/Ocultar sueldos**: Usa el toggle "Mostrar sueldo en la barra" para mostrar u ocultar los valores salariales.