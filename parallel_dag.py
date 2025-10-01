from airflow.decorators import dag, task
from time import sleep

@dag(schedule=None, catchup=False)
def parallel_dag():
    @task
    def task_1():
        print("Starting task 1")
        sleep(5)  # 30초에서 5초로 단축
        print("Task 1 completed")
        return 'Task 1 completed'

    @task
    def task_2():
        print("Starting task 2")
        sleep(5)  # 30초에서 5초로 단축
        print("Task 2 completed")
        return 'Task 2 completed'

    @task
    def task_3():
        print("Starting task 3")
        sleep(5)  # 30초에서 5초로 단축
        print("Task 3 completed")
        return 'Task 3 completed'
        
    @task
    def task_4():
        print('All parallel tasks completed')
        return 'Done'

    # 병렬 실행을 위해 >> 연산자 사용
    t1 = task_1()
    t2 = task_2()
    t3 = task_3()
    t4 = task_4()
    
    # t1, t2, t3가 병렬로 실행되고, 모두 완료되면 t4가 실행됨
    [t1, t2, t3] >> t4

parallel_dag()