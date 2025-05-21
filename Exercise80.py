
# Exercise 80: Shutil module
#The shutil module is a built-in module in Python that provides a way to
#perform high-level file operations such as copying, moving, and deleting files.
#It is a part of the standard library and does not require any additional installation.
import shutil
import os
#methods of shutils

#shutil.copy(src, dst)
#This method copies the contents of the source file to the destination file.
#If the destination file already exists, it will be overwritten.
shutil.copy("main.py", "main2.py")
#This will create a main2.py file and copy the contents of main.py to main2.py

#shutil.copy2(src, dst)
#This is similar to shutil.copy() but it also copies the metadata of the file such as the last modified time and permissions.

#shutil.copytree(src, dst)
#This method copies the entire directory tree from the source directory to the destination directory.
#If the destination directory already exists, it will raise an error.
shutil.copytree("dir", "dir1")

#shutil.move(src, dst)
#This method will move a file
#shutil.move(".tutorial/file.file", "file.file")

#shutil.rmtree(src)
# This method helps to delete a directory

#os.remove(src)
#  This method is  used to delete a file 

