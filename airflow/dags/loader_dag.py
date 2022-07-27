from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.email_operator import EmailOperator
import pandas as pd
import os
import sys
print(os.path.abspath("includes.............................."))
sys.path.append(os.path.abspath("includes"))

from loader import Warehouse
wr = Warehouse()
