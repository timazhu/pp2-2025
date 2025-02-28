#Write a Python program to convert a given camel case string to snake case.

import re
def camel_to_snake(text):
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
s = input()
print(camel_to_snake(s))

#ILikeBananas
#i_like_bananas