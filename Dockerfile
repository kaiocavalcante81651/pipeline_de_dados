FROM python:3.12-slim

WORKDIR /app

COPY . .

EXPOSE 5000

RUN pip install streamlit clickhouse-connect minio plotly

CMD ["streamlit", "run", "app.py", "--server.port=5000", "--server.address=0.0.0.0", "--browser.gatherUsageStats=false"]