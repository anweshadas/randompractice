#!/usr/bin/env python3
import os

dirpath = input("Enter a directory path: ")
filenames = os.listdir(dirpath)
bigsize = 0
name =""
for filename in filenames:
    filepath = os.path.join(dirpath,filename)
    filesize = os.path.getsize(filepath)
    if filesize > bigsize:
        bigsize = filesize
        name = filepath
print(f"The biggest file in the dirrectory is {name} and it's size is {bigsize}")



