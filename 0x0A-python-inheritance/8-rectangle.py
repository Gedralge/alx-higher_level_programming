#!/usr/bin/python3

"""
module for BaseGeometry/Rectangle.
"""

BaseGeometry = __import__('7-base_geomerty').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize"""
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
