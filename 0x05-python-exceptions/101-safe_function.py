#!/usr/bin/python3
import sys
def safe_function(fact, *args):
    try:
        res = fact(*args)
    except BaseException as e:
        res = None
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return res
