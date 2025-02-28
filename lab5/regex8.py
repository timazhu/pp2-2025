#Write a Python program to split a string at uppercase letters.

import re
text = input()
print(re.findall('[A-Z][^A-Z]*', text))

#UppercaseLetters
#['Uppercase', 'Letters']