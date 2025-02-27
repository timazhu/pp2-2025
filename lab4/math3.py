#Write a Python program to calculate the area of regular polygon.

from math import pi, tan
n = int(input())
a = int(input())
S = n / 4 * a ** 2 * 1 / tan(pi / n)
print(int(S))

#4
#25
#625