#  File: Cipher.py

#  Description: assignment 2

#  Student Name: Austin Yeh

#  Student UT EID: ay6922

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51135

#  Date Created: 02/05/2022

#  Date Last Modified: 02/05/2022

import math


# Input: n is an integer
# Output: function returns the minimum square integer that is greater than n
def min_greater_square(n):
    for i in range(n, n * (n + 1)):
        if math.sqrt(i) % 1 == 0:
            return i


# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string 
def encrypt(strng):
    new_strng = ''
    n = len(strng)
    side = int(math.sqrt(min_greater_square(n)))
    padded_strng = str(strng + '*' * (min_greater_square(n) - n))
    for i in range(side * (side - 1), side ** 2):
        for j in range(side):
            new_strng += padded_strng[i - side * j]
    return new_strng.replace('*', '')


# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string 
def decrypt(strng):
    new_strng = ''
    n = len(strng)
    side = int(math.sqrt(min_greater_square(n)))
    square = [[0 for i in range(side)] for j in range(side)]
    i = side ** 2 - len(strng)
    for c in range(side):
        for r in reversed(range(side)):
            if i == 0:
                break
            square[r][c] = '*'
            i -= 1
        else:
            continue
        break
    flatten_square = sum(square, [])
    index = 0
    for j in range(len(flatten_square)):
        if flatten_square[j] == 0:
            flatten_square[j] = strng[index]
            index += 1

    for i in reversed(range(side)):
        for j in range(side):
            new_strng += flatten_square[i + side * j]
    return new_strng.replace('*', '')


def main():
    # read the strings P and Q from standard input
    P, Q = input(), input()
    # encrypt the string P
    encrypted_P = encrypt(P)
    # decrypt the string Q
    decrypted_Q = decrypt(Q)
    # print the encrypted string of P
    # and the decrypted string of Q
    print(encrypted_P)
    print(decrypted_Q)


if __name__ == "__main__":
    main()
