# File: Triangle.py

# Description: A basic 2D Triangle class

# Student Name:

# Student UT EID:

# Course Name: CS 313E

# Unique Number: 86610

import sys
import math

TOL = 0.01

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
      self.x = x
      self.y = y

  # get the distance to another Point object
  def dist (self, other):
      return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

class Triangle (object):
    # constructor
    def __init__(self, PointA, PointB, PointC):
        self.A = PointA
        self.B = PointB
        self.C = PointC

    # check congruence of Triangles with equality
    # returns True or False (bolean)
    def __eq__(self, other):
        self_len = [self.A.dist(self.B), self.B.dist(self.C), self.C.dist(self.A)]
        other_len = [other.A.dist(other.B), other.B.dist(other.C), other.C.dist(other.A)]
        if sorted(self_len, key=lambda i: float(i)) == sorted(other_len, key=lambda i: float(i)):
            return True
        return False

    # returns whether or not the triangle is valid
    # returns True or False (bolean)
    def is_triangle(self):
        if self.A.dist(self.B) == self.B.dist(self.C) + self.C.dist(self.A) or self.B.dist(self.C) == self.A.dist(self.B) + self.C.dist(self.A) or self.C.dist(self.A) == self.A.dist(self.B) + self.B.dist(self.C):
            return False
        return True

    # return the area of the triangle:
    def area(self):
        # | [x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)]/2 |
        return abs(self.A.x * (self.B.y - self.C.y) + self.B.x * (self.C.y - self.A.y) + self.C.x * (self.A.y - self.B.y)) / 2

######################################################
# The code below is filled out for you, DO NOT EDIT. #
######################################################

# takes a string of coordinates and changes it to a list of Points
def get_points(coords_str):
    coords = [float(c) for c in coords_str.split(" ")]
    return [Point(c[0], c[1]) for c in zip(*[iter(coords)]*2)]

def main():
    # read the two triangles
    pointsA = get_points(sys.stdin.readline().strip())
    pointsB = get_points(sys.stdin.readline().strip())

    triangleA = Triangle(pointsA[0], pointsA[1], pointsA[2])
    triangleB = Triangle(pointsB[0], pointsB[1], pointsB[2])

    # Print final output
    print(triangleA.area())
    print(triangleB.area())
    print(triangleA.is_triangle())
    print(triangleB.is_triangle())
    print(triangleA == triangleB)

if __name__ == "__main__":
    main()
