# File: Anagrams.py

# Description: A program to group strings into anagram families

# Student Name: Austin Yeh

# Student UT EID: ay6922

# Course Name: CS 313E

# Unique Number: 51135

# Output: True or False
def are_anagrams(str1, str2):

    # Input: lst is a list of strings comprised of lowercase letters only
    # Output: the number of anagram families formed by lst
    return ''.join(sorted(str1)) == ''.join(sorted(str2))


def anagram_families(lst):
    dictionary = dict()
    for i in range(len(lst)):
        for key in dictionary.keys():
            if are_anagrams(lst[i], key):
                dictionary[key].append(lst[i])
                break
        else:
            dictionary[lst[i]] = [lst[i]]
    return len(dictionary.keys())


def main():
    # read the number of strings in the list
    num_strs = int(input())

    # add the input strings into a list
    lst = []
    for i in range(num_strs):
        lst += [input()]

    # compute the number of anagram families
    num_families = anagram_families(lst)

    # print the number of anagram families
    print(num_families)


if __name__ == "__main__":
    main()
