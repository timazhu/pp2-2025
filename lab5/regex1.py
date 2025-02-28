#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re
def text_match(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'YES'
        else:
                return("NO")
        
print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))

#NO
#NO
#YES
#YES
#YES