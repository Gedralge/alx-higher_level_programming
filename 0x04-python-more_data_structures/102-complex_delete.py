#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value in a dictionary
    """
    for i in list(a_dictionary.keys()):
        if a_dictionary[i] is value:
            del(a_dictionary[i])
            return a_dictionary
