#Exercise 79 :  Creating command line utility
#Command line utility is a program that runs in the command line
#and takes input from the user and returns output to the user
#In python you can create your own command line utility using the
# argparse module.
#The argparse module is a built-in module in Python that provides a way to
#parse command line arguments and options.

#example: curl --manual , is a command line utility

import argparse
import requests


parser = argparse.ArgumentParser()
#here we are creating an argument parser object

parser.add_argument("url", help="Url of the file to download")
#here we are adding an argument to the parser object

parser.add_argument("output", help="By which name you want to save your file")
#here we are adding an argument to the parser object

args = parser.parse_args()  
#here we are parsing the arguments


def download_file(url, local_filename):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename


print(args.url)
print(args.output)
#here we are printing the arguments
download_file(args.url, args.output)
#here we are calling the download_file function

#To run this program
#python Exercise79.py <url> <output>
#For example
#with image
#python Exercise79.py https://www.w3schools.com/w3images/fjords.jpg fjords.jpg