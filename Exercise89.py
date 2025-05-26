# Exercise 89: Multithreading

# Used when you want to parallely do some task
# In python we have import module as threading

import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds
'''
time1 = time.perf_counter()
# Normal code
# func(4)
# func(2)
# func(1)

# Same code using Threads
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])
t1.start()
t2.start()
t3.start()

# Calculating time
time2 = time.perf_counter()
print(time2 - time1)

'''
# concurrent.futures.Executor

def poolingDemo():
    with ThreadPoolExecutor() as executor:

        l = [3, 5, 1, 2]
        results = executor.map(func, l)
        for result in results:
            print(result)


poolingDemo()


