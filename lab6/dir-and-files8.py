#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

import os

file_path = "dir-and-files8.txt.txt"

if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"File {file_path} has been deleted.")
    else:
        print(f"No write access to {file_path}.")
else:
    print(f"File {file_path} does not exist.")

#File dir-and-files8.txt.txt has been deleted.