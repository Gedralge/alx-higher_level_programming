#!/usr/bin/python3

"""
This is a module for a class Rectanglr
"""


class Rectangle:
    """Class of a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize class"""
        self.__width = width
        self.__height = height

        @property
        def width(self):
            """Get width"""
            return self.__width

            @width.setter
            def width(self, value):
                if type(value) is not int:
                    raise TypeError("width must be an integer")
                if value < 0:
                    raise ValueError("width must be >= 0")
                self.__width = value

                @prorperty
                def height(self):
                    return self.__height

                @height.setter
                def height(self, value):
                    if type(value) is not int:
                        raise TypeError("height must be an integer")
                    if value < 0:
                        raise ValueError("height must be >= 0")
                    self.__height = value

                    def area(self):
                        return self.__width * self.__height

                    def perimeter(self):
                        if self.__width is 0 or self.__height is 0:
                            return 0
                        return (2 * self.__width) + (2 * self.__height)
