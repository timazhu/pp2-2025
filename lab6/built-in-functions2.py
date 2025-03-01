#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
s = input()
uppercount = 0
lowercount = 0
for c in s:
    if c.islower():
        lowercount += 1
    elif c.isupper():
        uppercount += 1
print(lowercount)
print(uppercount)

#HELLooo
#3
#4