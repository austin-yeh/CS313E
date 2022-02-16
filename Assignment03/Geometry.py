#  File: Geometry.py

#  Description:

#  Student Name: Austin Yeh

#  Student UT EID: ay6922

#  Partner Name: Eric Deng

#  Partner UT EID: cd36549

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
        return f"({float(self.x)}, {float(self.y)}, {float(self.z)})"

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

    # return a point that is the difference of two points
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    # return a point that is the sum of two points
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)


class Sphere(object):
    # constructor with default values
    def __init__(self, x=0.0, y=0.0, z=0.0, radius=1.0):
        self.center = Point(x, y, z)
        self.radius = radius

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__(self):
        return f"Center: ({float(self.center.x)}, {float(self.center.y)}, {float(self.center.z)}), Radius: {float(self.radius)}"

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
    # inside the Sphere/
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        cube_vertices = [a_cube.center + Point((-1) * a_cube.side / 2, (-1) * a_cube.side / 2, (-1) * a_cube.side / 2),
                         a_cube.center + Point((-1) * a_cube.side / 2, (-1) * a_cube.side / 2, a_cube.side / 2),
                         a_cube.center + Point((-1) * a_cube.side / 2, a_cube.side / 2, (-1) * a_cube.side / 2),
                         a_cube.center + Point((-1) * a_cube.side / 2, a_cube.side / 2, a_cube.side / 2),
                         a_cube.center + Point(a_cube.side / 2, (-1) * a_cube.side / 2, (-1) * a_cube.side / 2),
                         a_cube.center + Point(a_cube.side / 2, (-1) * a_cube.side / 2, a_cube.side / 2),
                         a_cube.center + Point(a_cube.side / 2, a_cube.side / 2, (-1) * a_cube.side / 2),
                         a_cube.center + Point(a_cube.side / 2, a_cube.side / 2, a_cube.side / 2)]
        for el in cube_vertices:
            if not self.is_inside_point(el):
                return False
        return True

    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl(self, a_cyl):
        try:
            # shifted_center = a_cyl.center - self.center
            # upper_limit = math.sqrt(math.pow(self.radius, 2) - math.pow(a_cyl.radius, 2)) - a_cyl.height / 2
            # lower_limit = math.sqrt(math.pow(self.radius, 2) - math.pow(a_cyl.radius, 2)) * (-1) + a_cyl.height / 2
            # return shifted_center.x ** 2 + shifted_center.y ** 2 + (a_cyl.height / 2) ** 2 < (
            #         self.radius - a_cyl.radius) ** 2 and lower_limit < shifted_center.z < upper_limit
            upper_sphere_xsection_r = math.sqrt(
                self.radius ** 2 - (a_cyl.center.z + a_cyl.height / 2 - self.center.z) ** 2)
            lower_sphere_xsection_r = math.sqrt(
                self.radius ** 2 - (a_cyl.center.z - a_cyl.height / 2 - self.center.z) ** 2)

            return upper_sphere_xsection_r > math.sqrt((self.center.x - a_cyl.center.x) ** 2 + (
                    self.center.y - a_cyl.center.y) ** 2) + a_cyl.radius and lower_sphere_xsection_r > math.sqrt(
                (self.center.x - a_cyl.center.x) ** 2 + (self.center.y - a_cyl.center.y) ** 2) + a_cyl.radius
        except ValueError:
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
        return Sphere(self.center.x, self.center.y, self.center.z, self.radius + a_cube.side).is_inside_point(
            a_cube.center) and not self.is_inside_cube(a_cube) and not a_cube.is_inside_sphere(self)

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube(self):
        return (Cube(self.center.x, self.center.y, self.center.z, 2 * self.radius / math.sqrt(3)))


class Cube(object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__(self, x=0, y=0, z=0, side=1.0):
        self.center = Point(x, y, z)
        self.side = side

    # string representation of a Cube of the form:
    # Center: (x, y, z), Side: value
    def __str__(self):
        return f"Center: {self.center}, Side: {float(self.side)}"

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
        cp1 = Point(a_cyl.center.x, a_cyl.center.y + a_cyl.height, a_cyl.center.z - a_cyl.radius)
        cp2 = Point(a_cyl.center.x, a_cyl.center.y + a_cyl.height, a_cyl.center.z + a_cyl.radius)
        cp3 = Point(a_cyl.center.x - a_cyl.radius, a_cyl.center.y + a_cyl.height, a_cyl.center.z)
        cp4 = Point(a_cyl.center.x + a_cyl.radius, a_cyl.center.y + a_cyl.height, a_cyl.center.z)
        cp5 = Point(a_cyl.center.x, a_cyl.center.y - a_cyl.height, a_cyl.center.z - a_cyl.radius)
        cp6 = Point(a_cyl.center.x, a_cyl.center.y - a_cyl.height, a_cyl.center.z + a_cyl.radius)
        cp7 = Point(a_cyl.center.x - a_cyl.radius, a_cyl.center.y - a_cyl.height, a_cyl.center.z)
        cp8 = Point(a_cyl.center.x + a_cyl.radius, a_cyl.center.y - a_cyl.height, a_cyl.center.z)
        return (self.is_inside_point(cp1) and self.is_inside_point(cp2) and self.is_inside_point(
            cp3) and self.is_inside_point(cp4) and self.is_inside_point(cp5) and self.is_inside_point(
            cp6) and self.is_inside_point(cp7) and self.is_inside_point(cp8))

    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, other):
        return Cube(self.center.x, self.center.y, self.center.z, self.side + other.side).is_inside_point(
            other.center) and not self.is_inside_cube(other) and not other.is_inside_cube(self)

    # determine the volume of intersection if this Cube
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume(self, other):
        vector = self.center - other.center
        # for each component of the vector, if the component is positive, then self component is greater than other component
        sides_of_intersection = []
        for el in [vector.x, vector.y, vector.z]:
            len = other.side / 2 - (vector.x - self.side / 2)
            if len <= 0:
                return 0.0
            sides_of_intersection.append(len)
        return math.prod(sides_of_intersection)

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
    def __init__(self, x=0, y=0, z=0, radius=1.0, height=1.0):
        self.center = Point(x, y, z)
        self.radius = radius
        self.height = height

    # returns a string representation of a Cylinder of the form:
    # Center: (x, y, z), Radius: value, Height: value
    def __str__(self):
        return f"Center: {self.center}, Radius: {float(self.radius)}, Height: {float(self.height)}"

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
        shifted_center = p - self.center
        return shifted_center.x ** 2 + shifted_center.y ** 2 < self.radius ** 2 and -self.height / 2 < shifted_center.z < self.height / 2

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        try:
            return Cylinder(self.center.x, self.center.y, self.center.z, self.radius - a_sphere.radius,
                            self.height - 2 * a_sphere.radius).is_inside_point(a_sphere.center)
        except ValueError:
            return False

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        cube_vertices = [a_cube.center + Point((-1) * a_cube.side / 2, (-1) * a_cube.side / 2, (-1) * a_cube.side / 2),
                         a_cube.center + Point((-1) * a_cube.side / 2, (-1) * a_cube.side / 2, a_cube.side / 2),
                         a_cube.center + Point((-1) * a_cube.side / 2, a_cube.side / 2, (-1) * a_cube.side / 2),
                         a_cube.center + Point((-1) * a_cube.side / 2, a_cube.side / 2, a_cube.side / 2),
                         a_cube.center + Point(a_cube.side / 2, (-1) * a_cube.side / 2, (-1) * a_cube.side / 2),
                         a_cube.center + Point(a_cube.side / 2, (-1) * a_cube.side / 2, a_cube.side / 2),
                         a_cube.center + Point(a_cube.side / 2, a_cube.side / 2, (-1) * a_cube.side / 2),
                         a_cube.center + Point(a_cube.side / 2, a_cube.side / 2, a_cube.side / 2)]
        for el in cube_vertices:
            if not self.is_inside_point(el):
                return False
        return True

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, other):
        z_overlap = min(self.center.z + self.height / 2, other.center.z + other.height / 2) - max(
            self.center.z - self.height / 2, other.center.z - other.height / 2)
        if z_overlap == other.height and self.radius > math.sqrt(
                math.pow(self.center.x - other.center.x, 2) + math.pow(self.center.y - other.center.y,
                                                                       2)) + other.radius:
            return True
        return False

    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder(self, other):
        if self.is_inside_cylinder(other) or other.is_inside_cylinder(self):
            return False
        return Cylinder(self.center.x, self.center.y, self.center.z, self.radius + other.radius,
                        self.height + other.height).is_inside_point(other.center)


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

    # print if the distance of p from the origin is greater
    # than the distance of q from the origin
    print(
        f"Distance of Point p from the origin \
{('is not', 'is')[p.distance(Point(0, 0, 0)) > q.distance(Point(0, 0, 0))]} \
greater than the distance of Point q from the origin")
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
    print(
        f"Volume of the largest Cube that is circumscribed by sphereA {('is not', 'is')[sphereA.circumscribe_cube().volume() > cylA.volume()]} greater than the volume of cylA")
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
    print(
        f"Intersection volume of cubeA and cubeB {('is not', 'is')[cubeA.intersection_volume(cubeB) > sphereA.volume()]} greater than the volume of sphereA")
    # print if the surface area of the largest Sphere object inscribed
    # by cubeA is greater than the surface area of cylA
    print(
        f"Surface area of the largest Sphere object inscribed by cubeA {('is not', 'is')[cubeA.inscribe_sphere().area() > cylA.area()]} greater than the surface area of cylA")
    # print if Point p is inside cylA
    print(f"Point p {('is not', 'is')[cylA.is_inside_point(p)]} inside cylA")
    # print if sphereA is inside cylA
    print(f"sphereA {('is not', 'is')[cylA.is_inside_sphere(sphereA)]} inside cylA")
    # print if cubeA is inside cylA
    print(f"cubeA {('is not', 'is')[cylA.is_inside_cube(cubeA)]} inside cylA")
    # print if cylB is inside cylA
    print(f"cylB {('is not', 'is')[cylA.is_inside_cylinder(cylB)]} inside cylA")
    # print if cylB intersects with cylA
    print(f"cylB {('does not', 'does')[cylA.does_intersect_cylinder(cylB)]} intersect cylA")
    # print(cylA.is_inside_cylinder(cylB))
    # print(cylB.is_inside_cylinder(cylA))


if __name__ == "__main__":
    main()
