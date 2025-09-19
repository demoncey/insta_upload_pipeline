FROM apache/airflow:2.9.2-python3.11

USER airflow
COPY --chown=airflow:airflow python/airflow/dags /opt/airflow/dags

# NIE polegamy na _AIRFLOW_WWW_USER_* w standalone
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False

# Bootstrap: migracja DB + idempotentne utworzenie admina + start standalone
CMD ["bash","-lc", "\
airflow db migrate && \
airflow users create \
  --username admin \
  --firstname DockerUser \
  --lastname DockerUser \
  --role Admin \
  --email admin@example.com \
  --password admin || true; \
exec airflow standalone"]
