#Write a Python program to list only directories, files and all directories, files in a specified path.

import os

def list_directories_files(path):
    print("Directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)

    print("\nFiles:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)

    print("\nAll Directories and Files:")
    for entry in os.listdir(path):
        print(entry)

path = "."

list_directories_files(path)

"""Files:
built-in-functions1.py
built-in-functions2.py
built-in-functions3.py
built-in-functions4.py
built-in-functions5.py
dir-and-files1.py

All Directories and Files:
built-in-functions1.py
built-in-functions2.py
built-in-functions3.py
built-in-functions4.py
built-in-functions5.py
dir-and-files1.py"""