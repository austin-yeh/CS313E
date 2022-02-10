#  File: Geometry.py

#  Description:

#  Student Name: Austin Yeh

#  Student UT EID: ay6922

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51135

#  Date Created: 2/7/2022

#  Date Last Modified: 2/7/2022

import math


class Point(object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    # test for equality between two points
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z


class Sphere(object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0, radius=1):
        self.center = Point(x, y, z)
        self.radius = radius

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__(self):
        return f"Center: {self.center}, Radius: {self.radius}"

    # compute surface area of Sphere
    # returns a floating point number
    def area(self):
        return 4 * math.pi * math.pow(self.radius, 2)

    # compute volume of a Sphere
    # returns a floating point number
    def volume(self):
        return 4 / 3 * math.pi * math.pow(self.radius, 3)

    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point(self, p):
        return self.center.distance(p) < self.radius

    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, other):
        return self.radius > self.center.distance(other.center) + other.radius

    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        return self.radius > math.pow(a_cube.side / 2, 2)

    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl(self, a_cyl):
        return False

    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere(self, other):
        return self.center.distance(other.center) < self.radius + other.radius and not self.is_inside_sphere(other)

    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, a_cube):
        return False

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube(self):
        return Cube(self.center.x, self.center.y, self.center.z, self.radius * math.sqrt(2))


class Cube(object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__(self, x=0, y=0, z=0, side=1):
        self.center = Point(x, y, z)
        self.side = side

    # string representation of a Cube of the form:
    # Center: (x, y, z), Side: value
    def __str__(self):
        return f"Center: {self.center}, Side: {self.side}"

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area(self):
        return math.pow(self.side, 2) * 6

    # compute volume of a Cube
    # returns a floating point number
    def volume(self):
        return math.pow(self.side, 3)

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point(self, p):
        return self.center.x + self.side / 2 > p.x > self.center.x - self.side / 2 \
               and self.center.y + self.side / 2 > p.y > self.center.y - self.side / 2 \
               and self.center.z + self.side / 2 > p.z > self.center.z - self.side / 2

    # determine if a Sphere is strictly inside this Cube
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        limit = self.side / 2 - a_sphere.radius
        return self.center.x - limit < a_sphere.center.x < self.center.x + limit \
               and self.center.y - limit < a_sphere.center.y < self.center.y + limit \
               and self.center.z - limit < a_sphere.center.z < self.center.z + limit and limit > 0

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube(self, other):
        limit = (self.side - other.side) / 2
        return self.center.x - limit < other.center.x < self.center.x + limit \
               and self.center.y - limit < other.center.y < self.center.y + limit \
               and self.center.z - limit < other.center.z < self.center.z + limit and limit > 0

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, a_cyl):
        return False

    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, other):
        return False

    # determine the volume of intersection if this Cube
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume(self, other):
        return 0.0

    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere(self):
        return Sphere(self.center.x, self.center.y, self.center.z, self.side / 2)


class Cylinder(object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__(self, x=0, y=0, z=0, radius=1, height=1):
        self.center = Point(x, y, z)
        self.radius = radius
        self.height = height

    # returns a string representation of a Cylinder of the form:
    # Center: (x, y, z), Radius: value, Height: value
    def __str__(self):
        return f"Center: {self.center}, Radius: {self.radius}, Height: {self.height}"

    # compute surface area of Cylinder
    # returns a floating point number
    def area(self):
        return 2 * math.pow(self.radius, 2) * math.pi + self.height * 2 * math.pi * self.radius

    # compute volume of a Cylinder
    # returns a floating point number
    def volume(self):
        return math.pi * math.pow(self.radius, 2) * self.height

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point(self, p):
        return False

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        return False

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        return False

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, other):
        return False

    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder(self, other):
        return False


def main():
    # read the coordinates of the first Point p
    input_lst = input().split(" ")
    p = Point(float(input_lst[0]), float(input_lst[1]), float(input_lst[2]))

    # read the coordinates of the second Point q
    input_lst = input().split(" ")
    q = Point(float(input_lst[0]), float(input_lst[1]), float(input_lst[2]))

    # read the coordinates of the center and radius of sphereA
    input_lst = input().split(" ")
    sphereA = Sphere(float(input_lst[0]), float(input_lst[1]), float(input_lst[2]), float(input_lst[3]))

    # read the coordinates of the center and radius of sphereB
    input_lst = input().split(" ")
    sphereB = Sphere(float(input_lst[0]), float(input_lst[1]), float(input_lst[2]), float(input_lst[3]))

    # read the coordinates of the center and side of cubeA
    input_lst = input().split(" ")
    cubeA = Cube(float(input_lst[0]), float(input_lst[1]), float(input_lst[2]), float(input_lst[3]))
    # read the coordinates of the center and side of cubeB
    input_lst = input().split(" ")
    cubeB = Cube(float(input_lst[0]), float(input_lst[1]), float(input_lst[2]), float(input_lst[3]))

    # read the coordinates of the center, radius and height of cylA
    input_lst = input().split(" ")
    cylA = Cylinder(float(input_lst[0]), float(input_lst[1]), float(input_lst[2]), float(input_lst[3]),
                    float(input_lst[4]))

    # read the coordinates of the center, radius and height of cylB
    input_lst = input().split(" ")
    cylB = Cylinder(float(input_lst[0]), float(input_lst[1]), float(input_lst[2]), float(input_lst[3]),
                    float(input_lst[4]))

    print(sphereA.circumscribe_cube())
    # print if the distance of p from the origin is greater
    # than the distance of q from the origin
    print(
        f"Distance of Point p from the origin \
{('is not', 'is')[p.distance(Point(0, 0, 0)) > q.distance(Point(0, 0, 0))]} \
greater than the distance of Point q from the origin")
    print()
    # print if Point p is inside sphereA
    print(f"Point p {('is not', 'is')[sphereA.is_inside_point(p)]} inside sphereA")
    # print if sphereB is inside sphereA
    print(f"sphereB {('is not', 'is')[sphereA.is_inside_sphere(sphereB)]} inside sphereA")
    # print if cubeA is inside sphereA
    print(f"cubeA {('is not', 'is')[sphereA.is_inside_cube(cubeA)]} inside sphereA")
    # print if cylA is inside sphereA
    print(f"cylA {('is not', 'is')[sphereA.is_inside_cyl(cylA)]} inside sphereA")
    # print if sphereA intersects with sphereB
    print(f"sphereA {('does not', 'does')[sphereA.does_intersect_sphere(sphereB)]} intersect sphereB")
    # print if cubeB intersects with sphereB
    print(f"cubeB {('does not', 'does')[sphereB.does_intersect_cube(cubeB)]} intersect sphereB")
    # print if the volume of the largest Cube that is circumscribed
    # by sphereA is greater than the volume of cylA
    print(f"Volume of the largest Cube that is circumscribed by sphereA (is / is not) greater than the volume of cylA")
    print()
    # print if Point p is inside cubeA
    print(f"Point p {('is not', 'is')[cubeA.is_inside_point(p)]} inside cubeA")
    # print if sphereA is inside cubeA
    print(f"sphereA {('is not', 'is')[cubeA.is_inside_sphere(sphereA)]} inside cubeA")
    # print if cubeB is inside cubeA
    print(f"cubeB {('is not', 'is')[cubeA.is_inside_cube(cubeB)]} inside cubeA")
    # print if cylA is inside cubeA
    print(f"cylA {('is not', 'is')[cubeA.is_inside_cylinder(cylA)]} inside cubeA")
    # print if cubeA intersects with cubeB
    print(f"cubeA {('does not', 'does')[cubeA.does_intersect_cube(cubeB)]} intersect cubeB")
    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA
    print(f"Intersection volume of cubeA and cubeB (is / is not) greater than the volume of sphereA")
    # print if the surface area of the largest Sphere object inscribed
    # by cubeA is greater than the surface area of cylA
    print(
        f"Surface area of the largest Sphere object inscribed by cubeA (is / is not) greater than the surface area of cylA")
    print()
    # print if Point p is inside cylA
    print(f"Point p (is / is not) inside cylA")
    # print if sphereA is inside cylA
    print(f"sphereA (is / is not) inside cylA")
    # print if cubeA is inside cylA
    print(f"cubeA (is / is not) inside cylA")
    # print if cylB is inside cylA
    print(f"cylB (is / is not) inside cylA")
    # print if cylB intersects with cylA
    print(f"cylB (does / does not) intersect cylA")


if __name__ == "__main__":
    main()
