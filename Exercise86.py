# Exercise 86: AsyncIO in Python

#  Asyncio is a Python built-in library used to write programs that run 
#  asynchronously- which means your program can di many tasks at once 
#  without waiting for each to finish.

# To handle many tasks at the same time (concurrent programming).
# To make your program faster and more efficient, especially when doing
# the I/O operations like: reading files, Calling APIs, Waiting for user IP, OP 

# Basic Keywords
# async def : defines an asynchronous function.
# await : tells Python to wait for the result of an async operation.
# asyncio.run() : runs the main async function.

import asyncio

async def say_Hello():
    print("Hello")
    await asyncio.sleep(2)  
    print("World")

asyncio.run(say_Hello())

# Multiple Tasks

async def task1():
    print("Task 1 started")
    await asyncio.sleep(3)
    print("Task 1 done")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 done")

async def main():
    await asyncio.gather(task1(),task2())
    # asyncio.gather is used to run multiple async function concurrently
asyncio.run(main())

# even though task1 takes longer , both tasks run concurrenty, saving time.


