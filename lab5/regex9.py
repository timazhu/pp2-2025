#Write a Python program to insert spaces between words starting with capital letters.

import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)
s = input()
print(capital_words_spaces(s))

#SpaceBetweenWords
#Space Between Words