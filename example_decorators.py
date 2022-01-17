from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)
        end_time = datetime.now()
        print('Execution time: {} seconds'.format(end_time - start_time))
    return wrapper

@execution_time
def random_func():
    for _ in range(1, int(1e8)):
        pass

@execution_time
def my_sum(a:int, b:int) -> int:
    return a + b

random_func()
my_sum(1, 2)

