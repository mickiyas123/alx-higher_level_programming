#!/usr/bin/python3

import json

""" Module 3-to_json_string that changes string to Json """


def to_json_string(my_obj):
    """ a function that returns the JSON representation
        of an object (string)

        Args:
            my_obj: data to be changed to json

        Return:
            Json representation of an object
    """
    return json.JSONEncoder().encode(my_obj)
