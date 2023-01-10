#!/usr/bin/python3
"""
Module to works on files with JSON
"""

import json


def save_to_json_file(my_obj, filename):
    """prints JSON representation of object to file"""
    with open(filename, "W") as f:
        js.dump(my_obj, f)
