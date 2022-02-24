#  File: Work.py

#  Description: Work.py

#  Student Name: Austin Yeh

#  Student UT EID: ay6922

#  Partner Name: Eric Deng

#  Partner UT EID: cd36549

#  Course Name: CS 313E

#  Unique Number: 51135

#  Date Created: 02/24/2022

#  Date Last Modified: 02/24/2022
import math
import sys
import time
import matplotlib.pyplot as plt


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series(v, k):
    p = 0
    summ = 0
    while v // k ** p != 0:
        summ += v // k ** p
        p += 1
    return summ


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search(n, k):
    lst = [sum_series(i, k) for i in range(n + 1)]
    for i in range(n + 1):
        if sum_series(i, k) >= n:
            print("Linear Search: ", i)
            return i


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search(n, k):
    lst = [sum_series(i, k) for i in range(n + 1)]
    low = 0
    high = n
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if sum_series(mid, k) < n:
            low = mid + 1
            try:
                if sum_series(mid + 1, k) >= n:
                    print("Binary Search: ", mid + 1)
                    return mid + 1
            except IndexError:
                pass
        elif sum_series(mid, k) > n:
            high = mid - 1
        else:
            print("Binary Search: ", mid)
            return mid
    return -1


def main():
    # read number of cases
    line = sys.stdin.readline()
    line = line.strip()
    num_cases = int(line)

    for i in range(num_cases):
        line = sys.stdin.readline()
        line = line.strip()
        inp = line.split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()


if __name__ == "__main__":
    main()
