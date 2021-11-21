#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print('')
    else:
        for row in matrix:
            for column in row:
                if column % 3 == 0:
                    print("{:d}".format(column))
                else:
                    print("{:d}".format(column), end = ' ')
