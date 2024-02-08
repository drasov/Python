import time

def decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        time_taken = start - end
        print("Start time: ", start)
        print("End time: ", end)
        print("Execution time: ", time_taken)
    return wrapper

@decorator
def timer():
    num = 0
    for i in range(1000):
        num + 1

timer()