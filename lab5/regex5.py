#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

text = input()
if re.search(r'a.*b$', text):
    print("YES")
else:
    print("NO")

#Baobab
#YES
#Bomba
#NO