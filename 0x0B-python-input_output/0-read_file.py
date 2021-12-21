#!/usr/bin/python3

""" Module 0-read_file.
Reads from a file and prints.
"""


def read_file(filename=""):
    """ function that reads a text file
        and prints it to stdout

        Args:
            filename: name of the file
    """

    with open("my_file_0.txt", encoding='utf-8') as a_file:
        print(a_file.read(), end="")
