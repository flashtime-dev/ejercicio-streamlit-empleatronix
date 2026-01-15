FROM python:3.10
RUN pip install streamlit pandas plotly
WORKDIR /app
ENTRYPOINT [ "streamlit", "run", "app.py" ]