#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    values = [val for val in a_dictionary.values() if val != value]
    a_dictionary = {key:val for key, val in a_dictionary.items() if val in values}
    return (a_dictionary)
