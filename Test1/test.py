def main():
    n = 4
    for i in range(n):
        for j in range(i, i+n**2, n):
            print(i, j)


main()
