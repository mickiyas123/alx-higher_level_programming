#!/usr/bin/python3

"""A square class with size attribute and exceptions"""


class Square:
    """A square class with size attribute and exceptions"""

    def __init__(self, size=0):
        """Inits Square.

        Args:
            size: size of a square
        """
        self.set_size(size)

    def set_size(self, size):
        """method to set check the value of size.

        Args:
            size: size of a square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
                
       
    
