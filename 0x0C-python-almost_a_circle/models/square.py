#!/usr/bin/python3
"""
This module implements a Square object
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square implementation"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(size, x, y, id)

        @property
        def size(self):
            """Size setter"""
            return self.__width

        @size.setter
        def size(self, value):
            """size setter"""
            self.width = value
            self.height = value

            def update(self, *args, **kwargs):
                """update the Square.

                Args:
                *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
                **kwargs (dict): New key/value pairs of attributes."""
                if args and len(args) != 0:
                    a = 0
                    for arg in args:
                        if a == 0:
                            if arg is None:
                                self.__init__(self.size, self.x, self.y)
                            else:
                                self.id = arg
                            elif a == 1:
                                self.size = arg
                            elif a == 2:
                                self.x = arg
                            elif a == 3:
                                self.y = arg
                                a += 1

                            elif kwargs and len(kwargs) != 0:
                                for k, v in kwargs.items():
                                    if k == "id":
                                        if v is None:
                                            self.__init__(self.size, self.x, self.y)
                                        else:
                                            self.id = v
                                        elif k == "size":
                                            self.size = v
                                        elif k == "x":
                                            self.x = v
                                        elif k == "y":
                                            self.y = v

                                            def to_dictionary(self):
                                                """Return the dictionary representation of the Square"""
                                                return {
                                                        "id": self.id,
                                                        "size": self.width,
                                                        "x": self.x,
                                                        "y": self.y
                                                        }

                                                def __str__(self):
                                                    Return the print() and str() representation of a Squqre"""
                                                    return "[square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
