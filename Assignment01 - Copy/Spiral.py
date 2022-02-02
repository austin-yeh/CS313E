def create_spiral(n):
    # making an empty matrix of the correct dimensions
    if (n % 2 == 0):
        n = n + 1
    matrix = []
    count = 0
    while (count < n):
        sMatrix = [0] * n
        matrix.append(sMatrix)
        count += 1
    # now, i'm going to fill that empty matrix to make the spiral
    # for the direction variable,
    insert = n ** 2
    IOne = 0
    while (IOne < (n + 1) / 2):
        spot = IOne
        # right to left
        while (spot < n - IOne):
            matrix[IOne][n - spot - 1] = insert
            insert -= 1
            spot += 1
        # down
        spot = IOne + 1
        while (spot < n - IOne):
            matrix[spot][IOne] = insert
            insert -= 1
            spot += 1
        # left to right
        spot = 1 + IOne
        while (spot < n - IOne):
            matrix[n - IOne - 1][spot] = insert
            insert -= 1
            spot += 1
        # up
        spot = 1 + IOne
        while (spot < n - IOne - 1):
            matrix[n - spot - 1][n - IOne - 1] = insert
            insert -= 1
            spot += 1
        IOne += 1
    return matrix


# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n, size):
    row = 0
    column = 0
    try:
        while (row < len(spiral)):
            if spiral[row].index(n) > -1:
                column = spiral[row].index(n)
                break
            row += 1
        sum = 0
        # left and right
        if (row - 1 > -1):
            sum += spiral[row][column]
        if (row + 1 < size):
            sum += spiral[row][column]
        if (column + 1 < size):
            if (row + 1 < size):
                sum += spiral[row + 1][column + 1]
            if (row - 1 > -1):
                sum += spiral[row - 1][column + 1]
        if (column - 1 > -1):
            if (row + 1 < size):
                sum += spiral[row + 1][column - 1]
            if (row - 1 > -1):
                sum += spiral[row - 1][column - 1]
        return (sum)
    except:
        print("cry")
        return ("")


def main():
    spiralDimension = int(input())
    spiral = create_spiral(spiralDimension)
    while True:
        try:
            sum = sum_adjacent_numbers(spiral, input(), spiralDimension)
            print(sum)
        except:
            pass


# read the input file

# create the spiral

# add the adjacent numbers

# print the result

if __name__ == "__main__":
    main()
