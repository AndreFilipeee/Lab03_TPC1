#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 13:42:42 2022

@author: carmen
To get and print a directory content
"""
import os
 
# get the list of all files and directories
dir_path = "."      # current path 
dir_list = os.listdir(dir_path)
 
print("Files and directories in '", dir_path, "' :")
 
# print all files and subdirs
print("ALL")
for x in dir_list:
    print(x)

# list to store files
res = []


# print files only
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

print("FILES")
for f in res: 
    print(f)
