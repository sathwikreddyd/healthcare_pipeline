from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 17),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'healthcare_data_pipeline',
    default_args=default_args,
    description='A simple healthcare data pipeline',
    schedule_interval=timedelta(days=1),
)

start_kafka_producer = DockerOperator(
    task_id='start_kafka_producer',
    image='python:3.8-slim',
    api_version='auto',
    auto_remove=True,
    command='python /usr/local/airflow/scripts/kafka_producer.py',
    docker_url='unix://var/run/docker.sock',
    network_mode='bridge',
    dag=dag,
)

start_spark_job = DockerOperator(
    task_id='start_spark_job',
    image='bitnami/spark:latest',
    api_version='auto',
    auto_remove=True,
    command='/bin/bash -c "spark-submit /usr/local/airflow/scripts/spark_consumer.py"',
    docker_url='unix://var/run/docker.sock',
    network_mode='bridge',
    dag=dag,
)

start_kafka_producer >> start_spark_job
