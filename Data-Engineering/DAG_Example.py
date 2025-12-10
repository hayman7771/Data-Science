
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "cameron",
    "start_date": datetime(2025, 1, 1),
}

with DAG(
    dag_id="simple_logging_dag",
    default_args=default_args,
    schedule_interval="@hourly",
    catchup=False,
) as dag:

    log_task = BashOperator(
        task_id="log_heartbeat",
        bash_command='echo "DAG is alive at $(date)"'
    )
