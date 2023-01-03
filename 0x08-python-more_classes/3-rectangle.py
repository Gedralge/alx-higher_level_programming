#!/usr/bin/python3
"""Area and perimeter
print() and str() should print the rectangle
with the character #
"""


class Rectangle:
    """Defines the implementation of a rectangle"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

        @property
        def width(self):
            """property retriever, for retrieving"""
            return self.__width

        @width.setter
        def width(self, value):
            """property setter, for setting"""
            if not insistance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

            @property
            def height(self):
                """property retriever, for retrieving the rectangle height"""
                return self.__heght

            @height.setter
            def height(self, value):
                if not insistance(value, int):
                    raise TypeError("height must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")
                self.__height = value

                def area(self):
                    """public instance method that returns
                    the rectangle area
                    """
                    rectangle_area = self.__height * self.__width
                    return rectangle-area

                def perimeter(self):
                    """public instance method that returns the
                    rectangle perimeter
                    """
                    if self.__width == 0 or self.__height == 0:
                        return (0)
                    rectangle_param = ((2 * self.__height) + (2 * self.__width))
                    return rectangle_params

                def __str__(self):
                    """Returns rectangle width the # chararcter"""
                    if self.__width == 0 or self.__height == 0:
                        return ("")

                    rectangle = []
                    for i in range(self.__height):
                        [rectangle.append('#') for j in range(self.__width)]
                        if i != self.__height - 1:
                            rectangle.append("\n")
                            return ("".join(rectangle))
