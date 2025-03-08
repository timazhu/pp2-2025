#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.

import os

def check_path_and_extract_components(path):
    if os.path.exists(path):
        print(f"'{path}' exists.")
        
        directory = os.path.dirname(path)
        filename = os.path.basename(path)
        
        print(f"Directory portion: {directory}")
        print(f"Filename portion: {filename}")
    else:
        print(f"'{path}' does not exist.")

path = input()

check_path_and_extract_components(path)

'''c:/Users/User/Desktop/PP2/lab6/dir-and-files1.py
'c:/Users/User/Desktop/PP2/lab6/dir-and-files1.py' exists.
Directory portion: c:/Users/User/Desktop/PP2/lab6
Filename portion: dir-and-files1.py'''