# Exercise 88: Function Caching in Python

# Function caching is a technique for improving the performance of a 
# program by storing the results of a function call so that you can 
# reuse the results instead of recomputing them. This is particularly
# useful for functions that are expensive to compute or that are called
# frequently with the same arguments.

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5) 
    return n * 5

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

# here the function does not take 5 seconds to run again
# it does memoization