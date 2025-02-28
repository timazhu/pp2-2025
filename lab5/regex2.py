#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re
def text_match(text):
        patterns = 'ab{2,3}'
        if re.search(patterns,  text):
                return 'YES'
        else:
                return('NO')
print(text_match("abc"))
print(text_match("aabbbcd"))

#NO
#YES