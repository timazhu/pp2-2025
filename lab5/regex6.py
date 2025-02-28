#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re
text = input()
result = re.sub(r'[ ,.]', ':', text)
print(result)

#Dairy products: milk, cheese, sour cream.
#Dairy:products::milk::cheese::sour:cream: