#Write the definition of a Point class. Objects from this class should have a

#a method show to display the coordinates of the point
#a method move to change these coordinates
#a method dist that computes the distance between 2 points

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

p1 = Point(3, 4)
p2 = Point(6, 8)

p1.show()
p2.show()

p1.move(7, 1)
p1.show()

distance = p1.dist(p2)
print(f"Distance between p1 and p2: {distance}")

#Point coordinates: (3, 4)
#Point coordinates: (6, 8)
#Point coordinates: (7, 1)
#Distance between p1 and p2: 7.0710678118654755