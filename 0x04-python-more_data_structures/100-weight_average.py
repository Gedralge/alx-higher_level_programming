#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Returns the weighed average of all integers tuple
    """
    if not my_list:
        return 0
    some = sum([x + y for x, y in my_list])
    return some / sum([y for x, y in my_list])
