
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from faker import Faker
def generate_fake_sensor_data():
    fake = Faker()
    sensor_data = {
        "sensor_id": fake.uuid4(),
        "timestamp": datetime.now().isoformat(),
        "temperature": fake.random_int(0, 100),
        "humidity": fake.random_int(10, 50),
        "pressure": fake.random_int(15, 100),
        "gas_level": fake.random_int(5, 30),
        "accelerometer_sensor": fake.random_int(3,70),
        "proximity_sensor": fake.random_int(1, 10)
    }
    return sensor_data


# Define the default arguments for the DAG
default_args = {
    'owner': 'vianney',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 21),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
# Define the DAG
dag = DAG(
    'fake_sensor_data',
    default_args=default_args,
    description='Generate fake sensor data',
    schedule_interval=timedelta(minutes=1),
)

# Define the tasks in the DAG
generate_sensor_data_task = PythonOperator(
    task_id='generate_sensor_data',
    python_callable=generate_fake_sensor_data,
    provide_context=True,
    dag=dag,
)

generate_sensor_data_task
