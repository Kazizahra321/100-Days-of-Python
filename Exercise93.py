# Exercise 93: Clear the clutter
# Python program to  clear the clutter inside a folder by renaming all the 
# PNG images from 1.png to n.png, where n is the number of PNG files in that folder.

import os
  # Get a list of all files in the folder
files = os.listdir("clutteredFolder")
    
i=1
for file in files:
        if file.endswith(".png"):
            print(file)
            os.rename(f"clutteredFolder/{file}",f"clutteredFolder/{i}.png")
            i = i+1
