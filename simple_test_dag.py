from airflow.decorators import dag, task

@dag(schedule=None, catchup=False)
def simple_test_dag():
    @task
    def hello_world():
        print("Hello World!")
        return "Hello World!"

    hello_world()

simple_test_dag()
