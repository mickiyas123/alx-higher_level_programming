#!/usr/bin/python3
""" Module base other moudlues inherit from """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ method for getting json representation
            of a the parameter list_dictionaries

            Args:
                list_dictionaries: List dictionaries

            Return:
                Json String representation
        """
        l_dict = []

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            for list_dictionarie in list_dictionaries:
                l_dict.append(list_dictionarie)
            return json.dumps(l_dict)

    @classmethod
    def save_to_file(cls, list_objs):
        """ method that writes json string representation
            of list_objs to a file

            Args:
                cls: current class
                list_objs: json string representation
        """
        filename = cls.__name__ + ".json"

        if list_objs is not None:
            new_list_obj = []

            for list_obj in list_objs:
                if isinstance(list_obj, cls):
                    new_list_obj.append(list_obj.to_dictionary())
            
            json_dict = json.loads(Base.to_json_string(new_list_obj))
            with open(filename, "w") as f:
                json.dump(json_dict, f)

        else:
            open(filename, "w").close()

    @staticmethod
    def from_json_string(json_string):
        """ method for that returns the list of the
            JSON string representation json_string

            Args:
                json_string: json string input

            Return:
                returns the list of the JSON string representation

        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ a class method that returns
            an instance with all attributes already set

            Args:
                dictionary: key word argument

            Return:
                returns an instance with all attributes already set

        """
        tr = cls(4, 5)
        for key, val in dictionary.items():
            tr.update(key=val)
        '''tr.update(x=dictionary['x'], y=dictionary['y'])
        tr.update(width=dictionary['width'], id=dictionary['id'])
        tr.update(height=dictionary['height'])'''
        return tr

    @classmethod
    def load_from_file(cls):
        """ class method that return list of instances

            Return:
                list of instances
        """
