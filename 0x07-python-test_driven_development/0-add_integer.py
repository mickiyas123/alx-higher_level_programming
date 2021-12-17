#!/usr/bin/python3
""" add_integer
    Adds two integer together
"""


def add_integer(a, b=98):
    """Function that adds two int.
       raise error if one of the
       input is not int or float

       Args:
            a: first value to be added
            b: second value to be added

        Return:
               sum of a and b
    """

    if type(a) is int or type(a) is float:
        a = int(a)
    else:
        raise TypeError('a must be an integer')
    if type(b) is int or type(b) is float:
        b = int(b)
    else:
        raise TypeError('b must be an integer')
    return a + b
