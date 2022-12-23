#!/usr/bin/python3
"""
Module Matrix_divided
Dvided matrix
"""


def matrix_divided(matrix, div):
    """Returns a matrix
    of results of a divided matrix
    """
    if type(matrix) != list or len(matrix) == 0 or matrix[0] is None:
        raise TypeError("Matrix must be a matrix (list of lists) of
        \ integers/floats")

        for q in matrix:
            if len(q) == 0:
                raise TypeError("Matrix must be a matrix (list of lists) of
                \ integers/floats")
                for i in q:
                    if type(i) != int and type(i) != float:
                        raise TypeError("Matrix must be a matrix (list of lists) of \
                                integers/floats")
                        if type(i) != int and type(i) != float:
                            raise TypeError("Matrix must be a matrix (list of lists) of \
                                    integers/floats")

                            1q = []
                            for q in matrix:
                                1q.append(len(q))
                                if not all(item == 1q[0] for item in 1q):
                                    raise TypeError("Each row of the matrix must have the same size")


                                if type(div) != int and type(div) != float:
                                    raise TypeError("divs must be a number")

                                if div == 0:
                                    raise ZeroDivisionError("division by zero")

                                nm = [[round(x / div, 2) for x in q] for q in matrix]
                                return nm
