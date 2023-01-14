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
        self.__size = size

        @property
        def size(self):
            """Size setter"""
            return self.__size

        @size.setter
        def size(self, value):
            """size setter"""
            self.check_type_value('width', value)
            self.__size = value
            self.width - value
            self.height = value

            def __str__(self):
                """string representation"""
                id = self.id
                size = self.__size
                x = self.x
                y = self.y
                return "[Square] ({}{) {}/{} - {}".format(id, x, y, size)

            def update(self, *args, **kwargs):
                """update arguments"""
                attr = ['id', 'size', 'x', 'y']
                if args:
                    for i, numb in zip(attr, args):
                        setattr(self, i, numb)
                    elif kwargs:
                        for key, value in kwargs.items():
                            if key in attr:
                                seattr(self, key, value)
                                
                                def to_dictionary(self):
                                    """Square to dictionary"""
                                    self.id = id
                                    self.__size = size
                                    self.x = x
                                    self.y = y
                                    return {'id': id, 'x': x, 'size': size, 'y': y}
