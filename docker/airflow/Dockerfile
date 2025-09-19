FROM apache/airflow:2.9.2-python3.11

# kopiujemy DAG-i do standardowej ścieżki
USER airflow
COPY --chown=airflow:airflow python/airflow/dags /opt/airflow/dags

# domyślnie uruchamiaj webserver (możesz nadpisać na 'scheduler')
CMD ["standalone"]
