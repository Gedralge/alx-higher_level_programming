#!/usr/bin/python3
"""defines the Rectangle class"""

from models.base import Base


def Rectangle(Base):
    """Rectangle implementation"""

    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """initialization"""
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            return self.__width

        @property
        def height(self):
            return self.__height

        @property
        def x(self):
            return self.__x

        @property
        def y(self):
            return self.__y

        @width.setter
        def width(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

            @height.setter
            def height(self, value):
                if type(value) is not int:
                    raise TypeError("height must be an integer")
                if value <= 0:
                    raise ValueError("height must be > 0")
                self.__height = value

                @x.setter
                def x(self, value):
                    if type(value) is not int:
                        raise TypeError("x must be an integer")
                    if value < 0:
                        raise ValueError("x must be >= 0")
                    self.__x = value

                @y.setter
                def y(self, value):
                    if type(value) is not int:
                        raise TypeError("y must be an integer")
                    if value < 0:
                        raise ValueError("y must be >= 0")
                    self.__x = value
                def area(self):
                    """returns the area of the rectangle"""
                    return self.width * self.height

                def display(self):
                    """display a rectangle with # filled space"""
                    for i in range(self.y):
                        print("")
                        for h in range(self.height):
                            for j in range(self.x):
                                print(" ", end="")
                                print("#" * self.width)

                                def __str__(self) -> str:
                                    """overwrites default"""
                                    return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))

                                def update(self, *args, **kwargs):
                                    """update attributes of class"""
                                    if args:
                                        try:
                                            self.id = args[0]
                                            self.width = args[1]
                                            self.height = args[2]
                                            self.x = args[3]
                                            self.y = args[4]
                                        except Exception:
                                            self
                                        elif kwargs:
                                            for attr, val in kwargs.items():
                                                if attr in dir(self):
                                                    setattr(self, attr, value)

                                                    def to_dictionary(self):
                                                        """dictionary representation"""
                                                        to_dict = {
                                                                "id": self.id,
                                                                "width": self.width,
                                                                "height": self.height,
                                                                "x": self.x,
                                                                "y": self.y
                                                                }
                                                        return to_dic
