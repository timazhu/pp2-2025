#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import os
import string

for letter in string.ascii_uppercase:
    file_path = os.path.join(os.getcwd(), f"{letter}.txt")
    with open(file_path, "w") as file:
        file.write(f"This is file {letter}.txt")