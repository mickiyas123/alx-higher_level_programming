#!/usr/bin/python3

""" A square class calcualting the size"""


class Square:
    """ A square class calcualting the size"""

    def __init__(self, size=0):
        """Inits Size.

        Args:
            size: size of the sqaure
        """
        self.set_size(size)

    def set_size(self, size):
        """ A method to set and check size.

        Args:
            size: size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ A method for calculating area"""
        return int(self.__size ** 2)
