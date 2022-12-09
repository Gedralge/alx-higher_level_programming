#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace all occurences of an element by another in a new list."""
    new = my_list.copy()
    for n, i in enumerate(new):
        if i == search:
            new[n] = replace
            return new
