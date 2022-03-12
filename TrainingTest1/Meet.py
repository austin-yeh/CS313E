#  File: Meet.py

#  Description: Determine earlist meet time interval for two people

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number: 86610

import sys


def earliestPossibleMeeting(person1, person2, duration):
    '''
        person1: List[List[int]]
        person2: List[List[int]]
        duration: int
        return type: List[int]
        '''
    person1 = sorted(person1, key=lambda x: x[0])
    person2 = sorted(person2, key=lambda x: x[0])
    for i in range(len(person1)):
        for j in range(len(person2)):
            if min(person1[i][1], person2[j][1]) - max(person1[i][0], person2[j][0]) >= duration:
                return [max(person1[i][0], person2[j][0]), max(person1[i][0], person2[j][0])+duration]

    return []


def main():
    # test_cases()

    # read the input data and create a list of lists for each person
    f = sys.stdin
    # read in the duration
    dur = int(f.readline().strip())
    # person 1's number of avalible slots
    num1 = int(f.readline().strip())
    p1 = []
    for x in range(num1):
        line = f.readline()
        l = line.strip().split()
        tmp = [int(l[0]), int(l[1])]
        p1.append(tmp)

    # person 2's number of avalible slots
    num2 = int(f.readline().strip())
    p2 = []
    for x in range(num2):
        line = f.readline()
        l = line.strip().split()
        tmp = [int(l[0]), int(l[1])]
        p2.append(tmp)

    print(earliestPossibleMeeting(p1, p2, dur))


if __name__ == "__main__":
    main()
