#!/usr/bin/python3
""" Module Rectangle """
from . import base


class Rectangle(base.Base):
    """ Rectangle class that inherits from base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle Init.

            Args:
                width: width of rectangle
                height: height of rectangle
                x,y: coordinate of rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ getter method for width """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter method for width """
        self.__width = width

    @property
    def height(self):
        """ getter method for height """
        return self.__height

    @height.setter
    def height(self, height):
        """ setter method for height """
        self.__height = height
