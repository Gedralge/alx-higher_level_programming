#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    maxi = my_lists[0]
    for i in my_list:
        if i > maxi:
            maxi = i
            return (maxi)
