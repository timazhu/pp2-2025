#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re
text = input()
matches = re.findall(r'\b[A-Z][a-z]+\b', text)
print(matches)

#Almaty is a beautiful city
#['Almaty']