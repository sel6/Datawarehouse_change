from airflow import DAG
from datetime import datetime
from airflow.operators.python_operator import PythonOperator
import os
import sys
print(os.path.abspath("includes.............................."))
sys.path.append(os.path.abspath("includes"))

from loader import Warehouse
wr = Warehouse()
    
def create_conn(**context):
    try:
        db = wr.DBConnect()
        print("succesfully created connection {}".format(db))
    except Exception as e:
        print(f'error...: {e}')

def create_table(**context):
    try:
        wr.createTables("includes/p_sql/schema.sql")
        print("successfully created tables!")
    except Exception as e:
        print(f'error...: {e}')

def load_data_to_table(**context):
    try:
        wr.insert_warehouse()
    except Exception as e:
        print(f'error...: {e}')

default_args = {"owner":"airflow","start_date":datetime(2021,3,7)}
with DAG(dag_id="orchesterate",default_args=default_args,schedule_interval='@daily', catchup=False) as dag:

    new_db_conn = PythonOperator(
        task_id = "create_db_connection",
        python_callable = create_conn,
        provide_context=True
    )

    new_table = PythonOperator(
        task_id = "create_new_table",
        python_callable = create_table,
        provide_context=True
    )

    fill_table = PythonOperator(
        task_id = "fill_table",
        python_callable = load_data_to_table,
        provide_context=True
    )

new_db_conn >> new_table >> fill_table