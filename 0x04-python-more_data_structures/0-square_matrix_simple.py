#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for a in matrix:
        squared = list(map(lambda x: x ** 2, a))
        new_matrix.append(squared)
    return new_matrix
