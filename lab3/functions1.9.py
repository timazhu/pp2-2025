#Write a function that computes the volume of a sphere given its radius

from math import pi

def Volume(R):
    V = 4 / 3 * pi * R ** 3
    return V

print(Volume(3))
#113.09733552923254