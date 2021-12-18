#!/usr/bin/python3

""" 2-matrix_divided module
    that divdes elemnts in a matrix
    in a given number
"""


def matrix_divided(matrix, div):
    """ matrix_divided function that
        divdes elements in a matrix

        Args:
            matrix: matrix
            div: number where each value elements will be dived by

        Return:
            A new matrix
    """
    message = 'matrix must be a matrix (list of lists) of integers/floats'

    new_matrix = [row[:] for row in matrix]

    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(div) == str:
        raise TypeError('div must be a number')

    first = len(new_matrix[0])

    for i in range(len(new_matrix)):
        if len(new_matrix[i]) != first:
            raise TypeError('Each row of the matrix must have the same size')
        for j in range(len(new_matrix[i])):
            if type(new_matrix[i][j]) is int:
                new_matrix[i][j] = round(new_matrix[i][j] / div, 2)
            elif type(new_matrix[i][j]) is float:
                new_matrix[i][j] = round(new_matrix[i][j] / div, 2)
            elif type(new_matrix[i][j]) is str:
                raise TypeError(message)
    return new_matrix
