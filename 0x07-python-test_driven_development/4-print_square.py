#!/usr/bin/python3

""" 4-print_square module that print sqaure of # """


def print_square(size):
    """ print_square function that prints square of #

        Args:
            size: size of the square
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) is float and type > 0:
        raise TypeError('size must be an integer')

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
