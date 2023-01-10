#!/usr/bin/python3
"""
Module for JSON serialization
"""


def class_to_json(obj):
    """Returns dictionary descriptiom with data list"""
    return obj.__dict__
