#!/usr/bin/python3

""" class Rectangle that defines a rectangle by: (based on 0-rectangle.py) """


class Rectangle:
    """ class variable """
    number_of_instances = 0
    print_symbol = "#"

    """ class that defines rectangle with some exception """

    def __init__(self, width=0, height=0):
        """Inits Square.

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """

        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """ A method for retriving width.

        Args:
            width: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """ A method for setting width.

        Args:
            width: width of the rectangle
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """ A method for retreving height

        Args:
            height: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """ A method for setting height rectangle.

        Args:
            height: height of the rectangle
        """
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """ A method for returning area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ A method for returning perimeter of a rectnagle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ A method for printing rectangle of # """
        newstr = ""
        if self.__height == 0 or self.__width == 0:
            return newstr
        for i in range(self.__height):
            for j in range(self.__width):
                newstr += Rectangle.print_symbol
            if i != self.__height - 1:
                newstr += "\n"
        return newstr

    def __repr__(self):
        """a method for string representation of the rectangle"""
        w = str(self.__width)
        h = str(self.__height)
        return "Rectangle(" + w + ", " + h + ")"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
