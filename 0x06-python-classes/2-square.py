#!/usr/bin/python3

"""Define a square."""

def __inint__(self, size=0):
    """Initialize a new Square.
    Args:
    size (int): The size of the new square.
    """
    if not insinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
