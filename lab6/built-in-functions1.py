#Write a Python program with builtin function to multiply all the numbers in a list

import math

def multiply(numbers):
    if not numbers:
        return 0
    return math.prod(numbers)

numbers = [1, 2, 3, 4, 5]
result = multiply(numbers)
print(result)