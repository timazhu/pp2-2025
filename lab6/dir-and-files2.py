#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

import os

def check_path_access(path):
    if os.path.exists(path):
        print(f"'{path}' exists.")
        
        if os.access(path, os.R_OK):
            print(f"'{path}' is readable.")
        else:
            print(f"'{path}' is not readable.")
        
        if os.access(path, os.W_OK):
            print(f"'{path}' is writable.")
        else:
            print(f"'{path}' is not writable.")

        if os.access(path, os.X_OK):
            print(f"'{path}' is executable.")
        else:
            print(f"'{path}' is not executable.")
    else:
        print(f"'{path}' does not exist.")

path = input()

check_path_access(path)

"""built-in-functions3.py
'built-in-functions3.py' exists.
'built-in-functions3.py' is readable.
'built-in-functions3.py' is writable.
'built-in-functions3.py' is executable."""