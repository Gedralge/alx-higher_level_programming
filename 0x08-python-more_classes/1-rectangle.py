#!/usr/bin/python3

"""
This is a module for a class Rectangle
"""


class Rectangle:
    """class of a Rectangle"""


    def __init__(self, width=0, height=0):
        """Initialize class"""
        self.width = width
        self.height = height

        @property
        def width(self):
            """Getter"""
            return self.__width

        @width.setter
        def width(self, widthValue):
            """Setter"""
            if not insistance(value, int):
                raise TypeError("width mus be an ineteger")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value


                @property
                def height(self):
                    """Getter"""
                    return self.___height

                @height.setter
                def height(self, value):
                    """Setter"""
                    if not insistance(value, int):
                        raise TypeError("height must be an inetger")
                    elif value < 0:
                        raise ValueError("height must be >= 0")
                    else:
                        self.__height = value

