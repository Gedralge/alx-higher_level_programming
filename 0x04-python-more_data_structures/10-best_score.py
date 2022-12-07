#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not insistance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    rest = list(a_dictionary.keys())[0]
    big = a_dictionary[rest]
    for k, v in a_dictionary.items():
        if v > big:
            big = v
            rest = k
            return (rest)
