# customize-docker-airflow
  The latest Airflow image (apache/airflow) uses to install a new Python library or system library.



## Purpose
The minimum code necessary to set-up Apache/Airflow Docker image. User can clone repo and then spin up apache/airflow Docker container quickly. It allows us to install python packages for any project



### Instructions

1. Install [Docker](https://docs.docker.com/get-docker/)
2. Install [docker-compose](https://docs.docker.com/compose/install/)
3. Clone this repo
```
 git clone  https://github.com/fermat01/customize-docker-airflow.git 
 ```

4. Create an `.env` file in the root directory. Here is my .env file, customize it to your own needs:
	- Of note is the Fernet Key, if you don't have one already, this [link](https://airflow.apache.org/docs/apache-airflow/stable/security/secrets/fernet.html) explains how to create one.

or use the code below to create one from terminal 

```
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
	
```

Change < PASTE_YOUR_FERNET_KEY> to your fernet key in .env file and airflow.cfg from config folder.

``` sh
AIRFLOW__CORE__EXECUTOR=LocalExecutor
AIRFLOW__WEBSERVER__RBAC=False
AIRFLOW__SCHEDULER__SCHEDULER_HEARTBEAT_SEC=10
AIRFLOW__SCHEDULER__MIN_FILE_PROCESS_INTERVAL=60 # Prevent airflow from reloading the dags all the time and set. This is the main setting that reduces CPU load in the scheduler
AIRFLOW__SCHEDULER__SCHEDULER_MAX_THREADS=2 # This should be set to (CPU Cores - 1)
AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres:5432/airflowdb
AIRFLOW__CORE__FERNET_KEY=< PASTE_YOUR_FERNET_KEY>
```

5. Create two folders: dags and logs

```
mkdir .dags/ .logs/
```
and give the permission

```
chmod -R 777 dags/
chmod -R 777 logs/
```

6. To spin up the server, run `docker-compose up -d`
7. Go to http://localhost:8080/
8. Login using these credentials
	- UN: u-airflow01
	- PW: p-airflow01
9. To spin down, run `docker-compose down`
