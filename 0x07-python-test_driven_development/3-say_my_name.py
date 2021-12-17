#!/usr/bin/python3

""" 3-say_my_name module that prints full name """


def say_my_name(first_name, last_name=""):
    """ say_my_name a function that prints
        first name and last name as a full name

        Args:
            first_name: First name of the full name
            last_name: Last name of the full nae
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
