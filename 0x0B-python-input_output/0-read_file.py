#!/usr/bin/python3
""" Module to read and print contents of a file """


def read_file(filename=""):

    """ Reads file and prints contents """
    with open(fiename, encoding="UTF-8") as f:
        string = f.read()
        print(string, end="")


