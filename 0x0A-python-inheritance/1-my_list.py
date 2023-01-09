#!/usr/bin/python3
"""
module for MyList
"""


class MyList(list):
    """MyuList class."""

    def print_sorted(self):
        """print the list sorted."""
        print(sorted(self))
