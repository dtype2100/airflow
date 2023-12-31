# from airflow import DAG
# import pendulum
# import datetime
# from airflow.operators.python import PythonOperator
# import random

# with DAG(
#     dag_id="dags_python_operator",
#     schedule="30 6 * *",
#     start_date=pendulum.datetime(2024, 1, 9, tz="Asia/Seoul"),
#     catchup=False,
# ) as dag:
#     def select_fruit():
#         fruit = ['APPLE', 'BANANA', 'ORANGE', 'AVOCADO']
#         rand_int = random.randint(0,3)
#         print(fruit[rand_int])

#     py_t1 = PythonOperator(
#         task_id = 'py_t1',
#         python_callable=select_fruit
#     )

#     py_t1

from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
import random

with DAG(
    dag_id="dags_python_operator",
    schedule_interval="30 6 * *",
    start_date=pendulum.datetime(2024, 1, 9, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    def select_fruit():
        fruit = ['APPLE', 'BANANA', 'ORANGE', 'AVOCADO']
        rand_int = random.randint(0, 3)
        print(fruit[rand_int])

    py_t1 = PythonOperator(
        task_id='py_t1',
        python_callable=select_fruit
    )

    # 의존성 설정
    py_t1
