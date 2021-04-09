import time


def speed_calc_decorator(function):
    def wrapper_function():
        start = time.time()
        function()
        end = time.time()
        print(f"{function.__name__} run speed: {end - start}s")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    total = 0
    for i in range(10000000):
        total += i * i
    print(total)
        
@speed_calc_decorator
def slow_function():
    total = 0
    for i in range(100000000):
        total += i * i
    print(total)

fast_function()
slow_function()
