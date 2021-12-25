#!/usr/bin/python3

""" Module base other moudlues inherit from """


class Base:
    """ Class Base other classes inherit from """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Base Inits.

            Args:
                id: integer value
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
