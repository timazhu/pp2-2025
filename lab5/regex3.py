#Write a Python program to find sequences of lowercase letters joined with a underscore.

import re
text = input()
matches = re.findall(r'\b[a-z]+_[a-z]+\b', text)
print(matches)

#I stil_remember the third_of_December
#['stil_remember']