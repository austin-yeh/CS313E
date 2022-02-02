#  File: Spiral.py

#  Description:

#  Student Name: Austin Yeh

#  Student UT EID: ay6922

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51135

#  Date Created: 01/25/2022

#  Date Last Modified: 01/25/2022

import sys


# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

def create_spiral(n):
    # creates 2D array full of 0's
    spiral = [[0 for i in range(n)] for j in range(n)]
    end_x, end_y = (n - 1) / 2, (n - 1) / 2
    x, y = 0, n - 1
    i = n ** 2
    # loop from top right corner counterclockwise until the center is reached
    while not (x == end_x and y == end_y):
        if x == 0 and y > 0:  # if on top edge, go left
            spiral[x][y] = i
            y -= 1
        elif y == 0 and x < n - 1:  # if on left edge, go down
            spiral[x][y] = i
            x += 1
        elif x == n - 1 and y < n - 1:  # if on bottom edge, go right
            spiral[x][y] = i
            y += 1
        elif y == n - 1 and x > 1:  # if on right edge, go up
            spiral[x][y] = i
            x -= 1
        elif spiral[x - 1][y] != 0 and spiral[x][y - 1] == 0:  # if above is filled and left isn't, go left
            spiral[x][y] = i
            y -= 1
        elif spiral[x][y - 1] != 0 and spiral[x + 1][y] == 0:  # if left is filled and below isn't, go down
            spiral[x][y] = i
            x += 1
        elif spiral[x + 1][y] != 0 and spiral[x][y + 1] == 0:  # if below is filled but right isn't, go right
            spiral[x][y] = i
            y += 1
        elif spiral[x][y + 1] != 0 and spiral[x - 1][y] == 0:  # if right is filled but above isn't, go up
            spiral[x][y] = i
            x -= 1
        i -= 1
    spiral[x][y] = i

    return spiral


# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    if n > len(spiral) ** 2:
        return 0
    else:
        indices = [0, 0]  # list of x and y indices of n
        for i in range(len(spiral)):  # finding index of n
            if n in spiral[i]:
                indices[0], indices[1] = i, spiral[i].index(n)

        # positions indicate index change in N, NW, W, SW, S, SE, E, NE directions
        positions = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
        # values indicate values in each direction
        values = [0, 0, 0, 0, 0, 0, 0, 0]

        i = 0
        for position in positions:  # in each direction
            try:  # trying document the value in the iterated position if the indices are valid
                values[i] = spiral[indices[0] + position[0]][indices[1] + position[1]] \
                    if indices[0] + position[0] >= 0 and indices[1] + position[1] >= 0 else 0
            except IndexError:
                pass
            i += 1
        return sum(values)


def main():
    # read the input file
    n = int(sys.stdin.readline())
    # create the spiral
    spiral = create_spiral(n)
    # iterate through values
    while True:
        try:
            n = int(sys.stdin.readline())
            # add and print values
            print(sum_adjacent_numbers(spiral, n))
        except ValueError:
            break


if __name__ == "__main__":
    main()
