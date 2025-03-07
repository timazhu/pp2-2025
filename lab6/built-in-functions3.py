#Write a Python program with builtin function that checks whether a passed string is palindrome or not.

s = input().lower()
s = ''.join(filter(str.isalnum, s))
if s[:] == s[::-1]:
    print('YES')
else:
    print('NO')

#Racecar
#YES