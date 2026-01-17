FROM python:3.10
RUN pip install streamlit pandas matplotlib
WORKDIR /app
ENTRYPOINT [ "streamlit", "run", "app.py" ]