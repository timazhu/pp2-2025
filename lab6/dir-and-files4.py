#Write a Python program to count the number of lines in a text file.

def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            count = 0
            for line in file:
                count += 1
        return count
    except FileNotFoundError:
        print(f"'{filename}' does not exist.")
        return None

filename = input()

num_lines = count_lines(filename)

if num_lines is not None:
    print(num_lines)

#c:/Users/User/Desktop/PP2/lab6/dir-and-files4.py
#19