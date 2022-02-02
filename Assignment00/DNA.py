#  File: DNA.py

#  Description: Assignment 0

#  Student Name: Austin Yeh

#  Student UT EID: ay6922

#  Partner Name: None

#  Partner UT EID: None

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 01/19/2022

#  Date Last Modified: 01/19/2022

from itertools import combinations
# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.
def longest_subsequence (s1, s2):
    lst = []
    len_lst = []
    possible_substrings = [s1[x:y] for x, y in combinations(range(len(s1) + 1), r=2)]
    for el in possible_substrings:
        if el in s2:
            lst.append(el)
            len_lst.append(len(el))
    return [lst[i] for i in range(len(lst)) if len_lst[i] == max(len_lst)]

def main():
    # read the data
    n = int(input())
    for i in range(n):
        s1 = input()
        s2 = input()
        # call longest_subsequence
        lst = longest_subsequence(s1, s2)
        if len(lst) == 0:
            print('No Common Sequence Found')
            continue
        # write out result(s)
        for item in sorted(list(set(lst))):
            print(item)
    # insert blank line
        print()

if __name__ == "__main__":
    main()
