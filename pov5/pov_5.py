import time


def delta_time(func):
    count_of_call = 0
    def wrapper( *args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        nonlocal count_of_call
        count_of_call += 1
        print(count_of_call)
        print(f"Time of execution: {end_time-start_time}")
        return result
    return wrapper

@delta_time
def counter(num):
    for x in range(num):
        pass


counter(10000000)
counter(1000000)