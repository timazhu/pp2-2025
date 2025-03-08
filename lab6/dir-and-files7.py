#Write a Python program to copy the contents of a file to another file

import os

source_path = "W.txt"
destination_path = "destination.txt"

if os.path.exists(source_path):
    with open(source_path, "r") as source_file:
        with open(destination_path, "w") as dest_file:
            dest_file.write(source_file.read())
    print(f"Contents copied from {source_path} to {destination_path}.")
else:
    print(f"Error: {source_path} does not exist.")

#Contents copied from W.txt to destination.txt.