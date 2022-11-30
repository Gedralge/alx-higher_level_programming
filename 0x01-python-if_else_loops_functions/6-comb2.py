#!/usr/bin/pyuthon3
for g in range(0, 10):
    for n in range(0, 10):
        if g >= n:
            continue
        elif g == 8 and n == 9:
            print("{}{}".format(g, n))
        else:
            print("{}{}, ".format(g, n), end='')
