#Write a Python program that invoke square root function after specific milliseconds.

import time
import math
def square_root(number, delay_ms):
    delay_s = delay_ms / 1000
    
    time.sleep(delay_s)
    
    result = math.sqrt(number)
    
    return result
number = 25100
delay_ms = 2123
square_root = square_root(number, delay_ms)
print(f"Square root of {number} after {delay_ms} milliseconds is {square_root}")

#Square root of 25100 after 2123 milliseconds is 158.42979517754858