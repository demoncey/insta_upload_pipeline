from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Simple Python function to be executed by the DAG
def hello_world():
    print("Hello from Airflow in App Runner!")

# Default arguments applied to all tasks in the DAG
default_args = {
    "owner": "you",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# DAG definition
with DAG(
    "hello_world",
    default_args=default_args,
    description="Test DAG for App Runner",
    schedule_interval=timedelta(minutes=10),  # run every 10 minutes
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["test"],
) as dag:
    # Single task that calls the hello_world() function
    PythonOperator(task_id="say_hello", python_callable=hello_world)
