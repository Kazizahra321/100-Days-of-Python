#Exercise87 
import time
import asyncio
import requests

async def function1():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram.ico", "wb").write(response.content)
    await asyncio.sleep(1)
    print("func 1")

async def function2():

    URL = "https://facebook.com/favicon.ico"
    response = requests.get(URL)
    open("facebook.ico", "wb").write(response.content)
    await asyncio.sleep(1)
    print("func 2")

async def function3():
    URL = "https://twitter.com/favicon.ico"
    response = requests.get(URL)
    open("twitter.ico", "wb").write(response.content)
    await asyncio.sleep(1)
    print("func 3")

async def main():
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)

asyncio.run(main())