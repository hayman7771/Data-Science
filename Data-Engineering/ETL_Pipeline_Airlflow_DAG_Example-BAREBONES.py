
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def extract(**context):
    # placeholder logic
    print("Extracting data...")
    return {"rows": 100}

def transform(**context):
    ti = context["ti"]
    extracted = ti.xcom_pull(task_ids="extract_task")
    print(f"Transforming {extracted['rows']} rows...")
    return {"rows": extracted["rows"], "valid_rows": int(extracted["rows"] * 0.95)}

def load(**context):
    ti = context["ti"]
    transformed = ti.xcom_pull(task_ids="transform_task")
    print(f"Loading {transformed['valid_rows']} valid rows into destination...")

default_args = {
    "owner": "cameron",
    "depends_on_past": False,
    "start_date": datetime(2025, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="example_etl_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract_task",
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id="transform_task",
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id="load_task",
        python_callable=load,
    )

    extract_task >> transform_task >> load_task
