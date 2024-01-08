from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
import random

with DAG(
    dag_id="dags_bash_select_fruit",
    schedule="30 6 * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    def select_fruit():
        fruit = ['APPLE', 'BANANA', 'ORANGE', 'AVOCADO']
        rand_id = random.randint(0,3)
        print(fruit[rand_id])

    py_t1 = PythonOperator(
        task_id = 'pt_t1',
        python_callable=select_fruit
    )

    py_t1