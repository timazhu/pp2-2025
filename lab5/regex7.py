#Write a python program to convert snake case string to camel case string.

import re
def snake_to_camel(word):
        return ''.join(x.capitalize() or '_' for x in word.split('_'))
s = input()
print(snake_to_camel(s))

#snake_case_string
#SnakeCaseString