#!/usr/bin/python3

""" A square class for calculating area of square"""


class Square:
    """A square class for calculating area of square"""

    def __init__(self, size=0):
        """Inits Square.

        Args:
            size: size of the square
        """
        self.size = size

    @property
    def size(self):
        """A method for retriving size.

        Args:
            size: size of the sqaure
        """
        return self.__size

    @size.setter
    def size(self, size):
        """A method for setting size with exceptions

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
        """A method for calculating area"""
        return int(self.__size ** 2)
