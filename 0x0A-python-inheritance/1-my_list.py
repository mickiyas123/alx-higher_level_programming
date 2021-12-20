#!/usr/bin/python3

""" 1-my_list module for inheriting a list """


class MyList(list):
    """ MyList drived class that inherits
        from superclass list
    """

    def print_sorted(self):
        """
        print sorted list

        """
        print(sorted(self))
