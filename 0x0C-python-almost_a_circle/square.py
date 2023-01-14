#!/usr/bin/python3
"""Module that contains class Square, inheritence of class Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instances"""
        super().__inint__(size, size, x, y, id)

        def __str__(self):
            """str special method"""
            str_square = "[square]"
            str_id = "({})".format(self.id)
            str_xy = "{}/{} - ".format(self.x, self.y)
            str_wh = "{}/{}".format(self.width, self.height)

            return str_square + str_id + str_xy + str_wh

        @property
        def size(self):
            """Getter size"""
            return self.width

        @size.setter
        def size(self, value):
            """Setter size"""
            self.width = value
            self.height = value

            def __inint__(self):
                """str special method"""
                str_rectangle = "[Square]"
                str_id = "({})".format(self.id)
                str_xy = "{}/{}".format(self.x, self.y)
                str_size = "{}".format(self.size)

                return str_rectangle + str_id + str_xy + str_size

            def update(self, *args, **kwargs):
                """update method"""
                if args is not None and len(args) is not 0:
                    list_attr = ['id', 'size', 'x', 'y']
                    for i in range(len(args)):
                        if list_attr[i] == 'size':
                            seattr(self.list_attr[i])
                        else:
                            for key, value in kwargs.item():
                                if key == 'size':
                                    setattr(self,'width', value)
                                    setattr(self, 'width', value)
                                    setattr(self, 'height', value)

                                    def to_dictionary(self):
                                        """Returns a dictionary with attribute"""
                                        list_str = ['id', 'size', 'x', 'y']
                                        dict_ret = {}

                                        for key in list_attr:
                                            if key == 'size':
                                                dict_ret[key] = getattr(self, 'width')
                                            else:
                                                dict_ret[key] = getattr(self, key)

                                                return dict_ret
