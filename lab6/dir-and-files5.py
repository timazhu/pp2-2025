#Write a Python program to write a list to a file.

my_list = ["apple", "banana", "peach", "cherry", "tangerine"]
with open("output.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")
print("File 'output.txt' has been created.")