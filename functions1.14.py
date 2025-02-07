def histogram(line):
    for star in line:
        print('*' * star)

histogram([23, 24, 25, 26, 27, 28])

#***********************
#************************
#*************************
#**************************
#***************************
#****************************


from math import pi

def Volume(R):
    V = 4 / 3 * pi * R ** 3
    return V

print(Volume((3 / pi) ** (1 / 3))) #3.999999999999999


def palindrome(s):
    s = ''.join([c for c in s if c.isalnum()]).lower()
    reversed_s = ""
    for i in range(len(s)-1, -1, -1):
        reversed_s += s[i]
    return s == reversed_s

print(palindrome("abababasababa")) #False


def permutations(s, start=0):
    if start == len(s) - 1:
        print(s)
        return

    for i in range(start, len(s)):
        s = list(s)
        s[start], s[i] = s[i], s[start]
        permutations(''.join(s), start + 1)
        s[start], s[i] = s[i], s[start]

print(permutations("1234"))

#1234
#1243
#1324
#1342
#1432
#1423
#2134
#2143
#2314
#2341
#2413
#3214
#3241
#3124
#3142
#3412
#3421
#4231
#4213
#4321
#4312
#4132
#4123