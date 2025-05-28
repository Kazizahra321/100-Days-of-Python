# Exercise 90 : Multiprocessing
# Used when you want to parallely do some task
# In python we have import module as multiprocessing

# This code downloads five images concurrently by creating five separate
# processes, each running the downloadFile function.

import multiprocessing  # Imports the multiprocessing module to create and manage multiple processes
import requests  # Imports the requests module to make HTTP requests
import os # Imports the os module to interact with the operating system, such as creating directories

def downloadFile(url, name):
    response = requests.get(url, verify=False)  # Makes an HTTP GET request to the specified URL and disables SSL verification
    # Check if the directory exists, if not, create it
    if not os.path.exists("files"):  # Checks if the "files" directory exists
        os.mkdir("files")  # Creates the "files" directory if it doesn't exist
    with open(f"files/file{name}.jpg", "wb") as file:  # Opens a file in the "files" directory with the name "file{name}.jpg" in write-binary mode
        file.write(response.content)  # Writes the content of the HTTP response to the file

url = "https://picsum.photos/200/300"  # Sets the URL variable to the URL of the image to be downloaded

if __name__ == "__main__":  # Ensures the following code runs only if the script is executed directly
    processes = []  # Initializes an empty list to store the process objects
    for i in range(5):  # Loops five times to create five processes
        p = multiprocessing.Process(target=downloadFile, args=(url, i))  # Creates a new process to run the downloadFile function with the arguments url and i
        processes.append(p)  # Adds the process object to the processes list
        p.start()  # Starts the process, which begins executing the downloadFile function

    for p in processes:  # Loops through the list of processes
        p.join()  # Waits for each process to complete before moving on to the next one

