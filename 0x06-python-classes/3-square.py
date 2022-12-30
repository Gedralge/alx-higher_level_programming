#!/usr/bin/python3
"""
Square module
"""


class Square:
    """
    Square define a geometric shape square

    Attributes:
    __size (int): the size of the square

    """
    def __int__(self, size=0):
        """
        Init method is a constructor for square class
        Args:
        size (int): the size of the square

        """
        self.__set(size)

            def __get(self):
                """
                Getter of instance attributes

                """
                return self.__size

            def ___set(self, size):
                """
                Setter of instance attributes

                Args:
                value (int): an integer assigned to the square size

                Raises:
                TypeError: if size is not an integer
                ValueError: if size is less than 0

                """
                if not type(size) is int:
                    raise TypeError("size must be an integer")
                if size < 0:
                    raise ValueError("size must be >= 0")
                else:
                    self.__size = size

                    def area(self):
                        """
                        Area returns the current square area

                        Returns:
                        integer: the square area

                        """
                        return self.__size**2
